from flask import Blueprint

api = Blueprint('api', __name__)

from . import posts, users, comments, errors, authentication
