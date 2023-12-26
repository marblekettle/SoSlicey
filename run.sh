PORT=8080
if ! test -d .venv; then
	make .venv
fi
if ! test -f .venv/bin/activate; then
	exit
fi
. .venv/bin/activate
mkdir instance
cp config.json instance
export FLASK_DEBUG=1
flask --app soslicey run --host="0.0.0.0" --port=$PORT