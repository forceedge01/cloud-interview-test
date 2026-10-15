serve:
	venv/bin/python main.py

database:
	docker-compose up

setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python -m alembic upgrade head

migration-sql:
	@if [ -z "$(FROM)" ] || [ -z "$(TO)" ]; then \
		echo "Usage: make migration-sql FROM=<from_revision> TO=<to_revision>"; \
		exit 1; \
	fi
	venv/bin/python -m alembic upgrade $(FROM):$(TO) --sql

ecr-login:
	aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

ecr-push:
	docker build -t "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:latest" .
	docker push "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:latest"
