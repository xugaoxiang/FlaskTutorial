from flask import Blueprint

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    return "Hello blueprint."