from flask import Blueprint, render_template
from ..db import getDb
from ..db.models import Item
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
bp = Blueprint('home', __name__)

@bp.route('/')
def home():
	return render_template('home.html')