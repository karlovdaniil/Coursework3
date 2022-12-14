import json


class CommentDAO:

    def __init__(self, path):
        """ При создании экземпляра dao указать путь к файлу с данными """
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self):
        """ Возвращает список со всеми комментариями """
        posts = self.load_data()
        return posts

    def get_by_post_id(self, post_id):
        """ Возвращает комментарии к конкретному посту """
        comments = self.load_data()
        comment = []
        for item in comments:
            if item['post_id'] == post_id:
                comment.append(item)
        return comment
