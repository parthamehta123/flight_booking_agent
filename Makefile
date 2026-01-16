run:
	python -m uvicorn app.api.main:app --reload

test:
	PYTHONPATH=. pytest

smoke:
	PYTHONPATH=. python scripts/smoke_test.py

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f
