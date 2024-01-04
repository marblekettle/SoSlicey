from flask import Blueprint, current_app
from ..db import initDb
from ..db.models import Item
from sqlalchemy.orm import Session

bp = Blueprint('test', __name__)

@bp.route('/test')
def test():
	return '<h1>Test</h1>'
