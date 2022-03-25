setup:
	git config commit.template .gitmessage.txt
	poetry install

clean:
	rm -vrf ./build ./dist ./*.tgz ./*.egg-info .pytest_cache 
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

test:
	poetry run pytest --cov=python_project