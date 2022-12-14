from app.posts.dao.posts_dao import PostsDAO

import pytest


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится он только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO('./data/posts.json')
    return posts_dao_instance


# Задаем, какие ключи ожидаем получить у поста
keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


class TestPostsDao:

    def test_get_all(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_all()
        assert type(posts) == list, 'возвращается не список'
        assert len(posts) > 0, 'возвращается пустой список'
        assert set(posts[0].keys()) == keys_should_be

    def test_get_by_pk(self, posts_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        post = posts_dao.get_by_pk(1)
        assert post['pk'] == 1, 'возвращается неправильный пост'
        assert set(post.keys()) == keys_should_be, 'не верный список ключей'
