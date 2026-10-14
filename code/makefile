database:
	docker-compose up

setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

serve:
	venv/bin/python main.py

migrate:
	venv/bin/python -m alembic upgrade head
