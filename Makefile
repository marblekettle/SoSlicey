SRC = soslicey/__init__.py

all: .venv

.venv: $(SRC)
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r req.txt

clean:
#	pip freeze > req.txt
	rm -rf .venv
	find . -name __pycache__ | xargs rm -rf

.phony: clean
