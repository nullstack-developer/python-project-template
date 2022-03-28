setup:
	git config commit.template .gitmessage.txt
	poetry install

clean:
	rm -vrf ./build ./dist ./*.tgz ./*.egg-info .pytest_cache 
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

format:
	poetry run isort .
	poetry run black .

typecheck:
	poetry run mypy .

lint:
	poetry run flake8

test:
	poetry run pytest --cov=python_project
