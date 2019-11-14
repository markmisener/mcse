SHELL := /bin/bash

.PHONY: install pre-commit

venv:
	virtualenv --python=python3.6 mcse-env

install: venv
	source mcse-env/bin/activate; \
	pip install -r requirements.txt; \

pre-commit: install
	source mcse-env/bin/activate; \
	pre-commit run --all-files
