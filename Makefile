POETRY_RUN := poetry run

reqs := requirements.txt requirements-dev.txt

.PHONY: all
all: clean install

# Virtual environments
.make.install.prod: poetry.lock
	poetry install --no-dev
	rm -f .make.install.*
	touch $@

.make.install.dev: poetry.lock
	poetry install
	rm -f .make.install.*
	touch $@

.PHONY: install
install: .make.install.prod

.PHONY: install-dev
install-dev: .make.install.dev

# Requirements
poetry.lock: pyproject.toml
	poetry lock

requirements.txt: poetry.lock
	poetry export --without-hashes -f requirements.txt -o $@

requirements-dev.txt: poetry.lock
	poetry export --dev --without-hashes -f requirements.txt -o $@

.PHONY: requirements
requirements: $(reqs)

# Utilities
.PHONY: tests
tests: test-lint test-unit

.PHONY: test-lint
test-lint: | .make.install.dev
	$(POETRY_RUN) flake8 image

.PHONY: test-unit
test-unit: | .make.install.dev
	$(POETRY_RUN) pytest -s --cov=image

clean:
	rm -f .make.install.*
	rm -rf .pytest_cache
	find . | grep __pycache__ | xargs rm -rf
	poetry env remove $$(poetry env list | egrep -o ".+\s")
