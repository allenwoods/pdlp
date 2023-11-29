setup:
	@poetry install

test:
	@poetry run pytest tests/

.PHONY: setup test