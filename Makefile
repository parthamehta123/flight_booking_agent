.PHONY: run test smoke up down logs lint format wait unit integration e2e

run:
	PYTHONPATH=. python -m uvicorn app.api.main:app --reload

test:
	PYTHONPATH=. pytest

unit:
	PYTHONPATH=. pytest tests/test_agent.py

integration:
	PYTHONPATH=. pytest tests/test_chat_integration.py

e2e:
	PYTHONPATH=. pytest tests/test_e2e.py

smoke:
	PYTHONPATH=. python scripts/smoke_test.py

up:
	docker compose up -d --build

wait:
	@echo "Waiting for API..."
	@until curl -s http://localhost:8000/health > /dev/null; do \
		sleep 1; \
	done
	@echo "API is ready"

down:
	docker compose down -v

logs:
	docker compose logs -f

lint:
	@python -m ruff check . || (echo "Ruff not installed. Run: pip install -r requirements-dev.txt" && exit 1)

format:
	@python -m ruff format . || (echo "Ruff not installed. Run: pip install -r requirements-dev.txt" && exit 1)
