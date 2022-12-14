from app.posts.dao.comment_dao import CommentDAO

import pytest


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится он только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def comment_dao():
    comment_dao_instance = CommentDAO('./data/comments.json')
    return comment_dao_instance


# Задаем, какие ключи ожидаем получить у комментария
keys_should_be = {'post_id', 'commenter_name', 'comment', 'pk'}


class TestCommentsDao:

    def test_get_all(self, comment_dao):
        """ Проверяем, верный ли список комментариев возвращается """
        comment = comment_dao.get_all()
        assert type(comment) == list, 'возвращается не список'
        assert len(comment) > 0, 'возвращается пустой список'
        assert set(comment[0].keys()) == keys_should_be

    def test_get_by_pk(self, comment_dao):
        """ Проверяем, верный ли комментарий возвращается при запросе одного """
        comments = comment_dao.get_by_post_id(1)
        print(comments)
        for comment in comments:
            assert comment['post_id'] == 1, 'возвращается неправильный комментарий'
        assert set(comment.keys()) == keys_should_be, 'не верный список ключей'
