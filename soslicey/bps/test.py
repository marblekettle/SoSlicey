from flask import Blueprint

bp = Blueprint('test', __name__)

@bp.route('/')
def test():
	return '<h1>TEST</h1>'