import json
from app.posts.dao.posts_dao import PostsDAO


class SearchDAO:

    def __init__(self, path):
        """ При создании экземпляра dao указать путь к файлу с данными """
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self):
        """ Возвращает список со всеми постами """
        posts = self.load_data()
        return posts

    def search_posts(self, s):
        """ Возвращает посты с искомым словом """
        posts = self.load_data()
        post = []
        for item in posts:
            if s in item['content']:
                post.append(item)
        return post

    def user_posts(self, username):
        """ Возвращает посты с искомым словом """
        posts = self.load_data()
        post = []
        for item in posts:
            if username in item['poster_name']:
                post.append(item)
        return post
