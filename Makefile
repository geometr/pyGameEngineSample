run: check
	python game.py

check:
	flake8 *.py
	pylint *.py
	mypy *.py

test:
	flake8 *.py | less
	pylint *.py | less
	mypy *.py | less

clean:
	rm -rf __pycache__
