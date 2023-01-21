import logging

# import app.bp_api.conflog as conflog
from app.bp_posts.dao.posts_dao import PostsDAO
from flask import Blueprint, jsonify, abort

# logging.basicConfig(level=logging.DEBUG,
#                     format=conflog.format,
#                     filename=conflog.filename,
#                     force=True)

# ----------------------------------------------------------------
# set up logging to console
# set up logging to file
logging.basicConfig(filename='./logs/api.log',
                    level=logging.INFO,
                    format='%(name)-12s: %(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
formatter = logging.Formatter('%(name)-12s: %(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)
# ----------------------------------------------------------------

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
        # raise ValueError
    logging.debug(f'Get one post #{post_id}')
    return jsonify(post), 200
