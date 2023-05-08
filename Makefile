setup: build publish package-f_install lint
install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain_calc
brain-gcd:
	poetry run brain_gcd
brain-prg:
	poetry run brain_progression	
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-f_install:
	pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games
