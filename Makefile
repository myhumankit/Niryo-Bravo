.PHONY: install
install:
	python -m virtualenv -p python2.7 venv
	venv/bin/pip install -r requirements.txt

.PHONY: serve
serve:
	FLASK_APP=niryo.py venv/bin/flask run --host.0.0.0 --port=8080
