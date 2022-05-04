all:
	@grep -Ee '^[a-z].*:' Makefile | cut -d: -f1 | grep -vF all

clean:
	- rm -rf gesture.egg-info/
	- rm -rf **/__pycache__
	- rm **/.DS_Store
	- rm -rf build/ dist/

test:
	python -m unittest
	
build: clean
	python setup.py sdist bdist_wheel
