from flask import Blueprint, render_template

bp = Blueprint('test', __name__)

@bp.route('/')
def test():
	return render_template('base.html')