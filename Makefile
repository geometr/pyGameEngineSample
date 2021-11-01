run: check
	python game.py

check:
	flake8 .

test:
	flake8 . | less

clean:
	rm -rf __pycache__
