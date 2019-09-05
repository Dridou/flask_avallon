from flask import Blueprint, jsonify

from app import url_prefix

reservation_blueprint = Blueprint('reservation', __name__, url_prefix='/reservation')

@reservation_blueprint.route('/', methods=['GET'])
def state_of_reservations():
    return jsonify("this is state of reservations")
