from flask import Blueprint, render_template
from .dao.posts_dao import PostsDAO
from .dao.comment_dao import CommentDAO

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

# Создаем dao
posts_dao = PostsDAO('./data/posts.json')
comment_dao = CommentDAO('./data/comments.json')


# Создаем вьюшку для постов
@posts_blueprint.route('/')
def page_posts_all():
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)


# Создаем вьюшку для одного поста по номеру
@posts_blueprint.route('/posts/<int:pk>/')
def page_post(pk):
    post = posts_dao.get_by_pk(pk)
    comments = comment_dao.get_by_post_id(pk)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)
