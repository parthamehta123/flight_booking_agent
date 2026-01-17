.PHONY: run test smoke up down logs lint format wait unit integration e2e

run:
	PYTHONPATH=. python -m uvicorn app.api.main:app --reload

test:
	PYTHONPATH=. pytest -m "not e2e"

ci:
	PYTHONPATH=. pytest

unit:
	PYTHONPATH=. pytest tests/test_agent.py

integration:
	PYTHONPATH=. pytest tests/test_chat_integration.py

e2e:
	PYTHONPATH=. pytest -m e2e

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

doctor:
	@echo "🔍 Running environment diagnostics..."
	@python -c "from app.config.settings import settings; \
	print('ENV:', settings.env); \
	print('USE_POSTGRES:', settings.use_postgres); \
	print('MEMORY_BACKEND:', settings.memory_backend); \
	print('API_TOKEN set:', bool(settings.api_token)); \
	print('DATABASE_URL set:', bool(settings.database_url))"
