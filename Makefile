run:
	python runner.py
test:
	python -m pytest -svv app/tests/test_main.py --disable-warnings
