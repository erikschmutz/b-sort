venv:
	python3 -m venv venv

install: requirements.txt
	venv/bin/python3 -m pip install -r requirements.txt

start: venv install
	FLASK_ENV=development venv/bin/flask run

test:
	python3 -m unittest  app_test
