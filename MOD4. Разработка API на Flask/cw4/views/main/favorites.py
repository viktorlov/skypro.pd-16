# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import request
from flask_restx import Namespace, Resource

from container import favorite_movie_service, user_service, movie_service
from services.auth_service import auth_required
# from setup.api.models import favorite_movie

api = Namespace('favorites')


@api.route('/movies/<int:movie_id>/')
class FavoritesView(Resource):
    # @api.marshal_with(favorite_movie, as_list=True, code=200, description='OK')
    @auth_required
    def post(self, movie_id):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
        user = user_service.get_user_by_token(token)
        return favorite_movie_service.add_movie(user_id=user.id, movie_id=movie_id)

    # @api.marshal_with(favorite_movie, as_list=True, code=200, description='OK')
    @auth_required
    def delete(self, movie_id):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
        user = user_service.get_user_by_token(token)
        return favorite_movie_service.delete_movie(user_id=user.id, movie_id=movie_id)
