.PHONY: format lint test type clean

format:
	black .
	isort .

lint:
	flake8 .

type:
	mypy .

test:
	pytest

check: format lint type test

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -f .coverage