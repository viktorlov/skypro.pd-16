import pytest
from app.bp_posts.dao.posts_dao import PostsDAO


@pytest.fixture()
def posts_dao():
    posts_dao_pattern = PostsDAO('./data/posts.json')
    return posts_dao_pattern


original_keys = {'poster_name',
                 'poster_avatar',
                 'pic',
                 'content',
                 'views_count',
                 'likes_count',
                 'pk',
                 }


class TestPostsDAO:

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == original_keys, "неверный список ключей"

    def test_get_by_pk(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert post[0]["pk"] == 1, "возвращается неправильный пост"
        assert set(post[0].keys()) == original_keys, "неверный список ключей"
