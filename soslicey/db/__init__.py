from sqlalchemy import create_engine
from flask import current_app, g
from .models import Base

def getDb():
	with current_app.app_context():
		try:
			if 'db' not in g:
				g.db = {}
				g.db['engine'] = create_engine(
					current_app.config['DATABASE'], echo=True)
		except Exception as e:
			print(e.message())
			g.db = None
		finally:
			return g.db

def initDb():
	db = getDb()
	meta = Base.metadata
	with db['engine'].connect() as conn:
		meta.create_all(db['engine'])
	return db

