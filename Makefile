.PHONY: install
install:
	python -m virtualenv -p python2.7 venv
	venv/bin/pip install -r requirements.txt