# Init vars
MAKEFILE := $(lastword $(MAKEFILE_LIST))
BASENAME := $(shell basename "$(PWD)")
SHELL := /bin/bash

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Commands:"
	@echo
	@sed -n 's/^##//p' $< | sed -e 's/^/ /' | sort
	@echo

## setup              Create env and install project requirements.
setup:
	python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt

## setup              Create env and install project requirements.
migratedb:
	python3 -m venv venv && . venv/bin/activate && python manage.py makemigrations src && python manage.py migrate

run:
	@if [ -z "$(DOCKER_IMAGE)" ]; then \
		DOCKER_IMAGE=$(eval DOCKER_IMAGE=$(BASENAME):latest); \
	fi
	docker build -f Dockerfile -t $(BASENAME) .
	docker run --rm -it -p 8888:8888 $(BASENAME):latest




