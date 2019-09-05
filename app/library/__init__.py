from flask import Blueprint, jsonify

from app import url_prefix

library_blueprint = Blueprint('library', __name__, url_prefix = '/library')


@library_blueprint.route('/', methods=['GET'])
def state_of_the_library():
    return jsonify("this is the state of the library")
