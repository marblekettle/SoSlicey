if ! test -d .venv; then
	make .venv
fi
if ! test -f .venv/bin/activate; then
	exit
fi
. .venv/bin/activate
export FLASK_DEBUG=1
flask --app soslicey run