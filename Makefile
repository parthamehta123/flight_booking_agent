run:
	uvicorn app.api.main:app --reload

test:
	pytest