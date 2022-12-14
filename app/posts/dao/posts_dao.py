import json


class PostsDAO:

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

    def get_by_pk(self, pk):
        """ Возвращает один пост по его номеру """
        posts = self.load_data()
        for post in posts:
            if post['pk'] == pk:
                return post
