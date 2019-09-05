from flask import Blueprint, jsonify

from app import url_prefix

book_blueprint = Blueprint('book', __name__, url_prefix = '/book')

@book_blueprint.route('/', methods=['GET'])
def state_of_books():
    return jsonify("this is state of book")

