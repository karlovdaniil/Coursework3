from flask import Blueprint, render_template, request

from app.search.dao.search_dao import SearchDAO

# Создаем блупринт
search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')

# Создаем dao
search_dao = SearchDAO('./data/posts.json')


# Создаем вьюшки для постов
@search_blueprint.route('/search')
def page_posts_search():
    s = request.args.get('s')
    found_posts = search_dao.search_posts(s)
    if s:
        return render_template('search.html', s=found_posts)


@search_blueprint.route('/users/<username>')
def user_search(username):
    user_posts = search_dao.user_posts(username)
    return render_template('user-feed.html', user_posts=user_posts, username=username)
