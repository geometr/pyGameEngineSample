run:
	python game.py
test: clean check coverage

check: 
	flake8 *.py
	pylint *.py
	mypy *.py

clean:
	rm -rf __pycache__

coverage:
	coverage erase
	coverage run -m pytest -ra
	coverage report -m  
