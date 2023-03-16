# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from setup.api.models import movie
from setup.api.parsers import page_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        filter = request.args.get('status')
        if filter != None and filter == 'new':
            return movie_service.get_all(filter=filter, **page_parser.parse_args())
        else:
            return movie_service.get_all(**page_parser.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)
