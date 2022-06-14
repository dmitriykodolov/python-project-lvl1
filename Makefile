install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

build:
	poetry build

publish: 
	poetry publish --dry-run #публикуем

package-install: 
	python3 -m pip install --user dist/*.whl

pack-re:
	python3 -m pip install --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games


