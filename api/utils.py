import json


def load_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts_data = json.load(file)
        return posts_data


def get_post_by_pk(pk):
    posts = load_posts()

    for post in posts:
        if post['pk'] == pk:
            return post

    return f'Пост не найден'
