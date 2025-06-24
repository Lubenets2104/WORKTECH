set shell := ["cmd", "/C"]  

up:
	uvicorn app.main:app --reload

test:
	pytest tests/

lint:
	ruff app tests
