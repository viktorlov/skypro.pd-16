from flask import request
from flask_restx import Resource, Namespace

from models import Review
from setup_db import db

review_ns = Namespace('reviews')


@review_ns.route('/')
class ReviewsView(Resource):
    def get(self):
        reviews = Review.query.all()
        result = []
        for review in reviews:
            temp = review.__dict__
            del temp['_sa_instance_state']
            result.append(temp)
        return result, 200

    def post(self):
        json_request = request.json
        temp = Review(**json_request)
        try:
            db.session.add(temp)
            db.session.commit()
            return "", 201
        except Exception as e:
            return {'message': str(e)}, 500

@review_ns.route('/<int:rid>/')
class ReviewView(Resource):
    def get(self, rid):
        review = Review.query.get(rid)
        try:
            result = review.__dict__
            del result['_sa_instance_state']
            return result, 200
        except Exception as e:
            return {'message': str(e)}, 500

    def put(self, rid):
        updated_review = db.session.query(Review).filter(Review.id == rid).update(request.json)
        if not updated_review:
            return f"Читатель с индексом {rid} не найден.", 400
        db.session.commit()
        return "", 204

    def delete(self, rid):
        deleted_review = Review.query.get(rid)
        try:
            db.session.delete(deleted_review)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500
