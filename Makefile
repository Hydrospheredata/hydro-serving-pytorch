PYTHON=python

VERSION=$(shell cat ./version)

image-cpu:
	docker build -t hydrosphere/serving-runtime-pytorch:$(VERSION)-cpu -f ./docker/cpu.Dockerfile .

test:
	$(PYTHON) setup.py test