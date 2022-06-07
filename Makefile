install:
	poetry install # установить poetry

brain-games: # запускаем модуль>
	poetry run brain-games

build: # создаем дистрибутив??
	poetry build

publish: 
	poetry publish --dry-run #публикуем

package-install: 
	python3 -m pip install --force-reinstall dist/*.whl  # устанавливаем себе пакет




