all:
	python setup.py sdist

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	rm -rf build/
	rm -rf dist/
	rm -rf adhs.egg-info/
