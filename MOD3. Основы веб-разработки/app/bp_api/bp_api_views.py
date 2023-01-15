from app.bp_posts.dao.posts_dao import PostsDAO
from flask import Blueprint, jsonify, abort

### logging

import logging
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] [%(message)s]', filename='./logs/api.log')


api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO('./data/posts.json')


@api_blueprint.get('/api/posts/')
def api_index():
    logging.debug('Get all posts')
    posts: list[dict] = posts_dao.get_all()
    return jsonify(posts), 200


@api_blueprint.get('/api/posts/<int:post_id>/')
def api_post(post_id):
    post: list[dict] = posts_dao.get_by_pk(post_id)
    if post == [{}]:
        logging.error('Post not found')
        abort(500, description='ValueError > post_id is out of range.')
    logging.debug(f'Get one post #{post_id}')
    return jsonify(post), 200
