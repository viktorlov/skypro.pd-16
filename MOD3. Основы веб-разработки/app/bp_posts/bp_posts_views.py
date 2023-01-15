from flask import Blueprint, abort, render_template, request

from .dao.comments_dao import CommentsDAO
from .dao.posts_dao import PostsDAO

# создаём блюпринт для постов
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

# создаём DAO
posts_dao = PostsDAO('./data/posts.json')
comments_dao = CommentsDAO('./data/comments.json')


# создаём представление для всех постов
@posts_blueprint.get('/')
def get_posts_all():
    posts: list[dict] = posts_dao.get_all()
    return render_template('index.html', posts=posts)


# создаём представление для одного поста
@posts_blueprint.get('/post/<int:post_id>/')
def get_post_by_pk(post_id):
    post: list[dict] = posts_dao.get_by_pk(post_id)
    comment_s: list[dict] = comments_dao.get_by_post_id(post_id)
    if comment_s[0] == post[0]:
        abort(500, description="ValueError: post_id is out of range")
    tag_s: list[str] = []
    for word in post[0]['content'].split(' '):
        if word.startswith('#'):
            tag_s.append(word)
    return render_template('post.html', post=post[0], comments=comment_s, lencom=len(comment_s), tags=tag_s)


# создаём представление для одного пользователя
@posts_blueprint.get('/user/<user_name>/')
def get_posts_by_user(user_name):
    post_s: list[dict] = posts_dao.get_by_user(user_name)
    return render_template('user-feed.html', posts=post_s, user=user_name)


# создаём представление для поиска
@posts_blueprint.get('/search/')
def get_search():
    query: str = request.args.get("s")
    post_s: list[dict] = posts_dao.search(query)
    return render_template("search.html", posts=post_s, poslen=len(post_s))

@posts_blueprint.get('/tag/<tagname>/')
def get_posts_by_tag(tagname):
    post_s: list[dict] = posts_dao.get_by_tag(tagname)
    return render_template('tag.html', tag = tagname, posts = post_s)