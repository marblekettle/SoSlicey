from flask import Flask
from .bps import bps
import json

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	if test_config is None:
		app.config.from_file('config.json', load=json.load)
	else:
		app.config.from_mapping(test_config)
	for bp in bps:
		app.register_blueprint(bp)
	return app