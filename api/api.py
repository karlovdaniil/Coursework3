import logging
from flask import Blueprint, jsonify

from api.utils import load_posts, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)

logging.basicConfig(filename='api/logs/api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


@api_blueprint.route('/api/posts')
def get_all_posts():
    logging.info
    return jsonify(load_posts())


@api_blueprint.route('/api/posts/<int:postid>')
def get_post_by_id(postid):
    logging.info
    return jsonify(get_post_by_pk(postid))
