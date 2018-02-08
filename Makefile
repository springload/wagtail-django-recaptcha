.PHONY: clean-pyc init help test-ci
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'

init: clean-pyc ## Install dependencies and initialise for development.
	pip install -e .[testing,docs] -U

lint: ## Lint the project.
	flake8 wagtailcaptcha setup.py

test: ## Test the project.
	python ./runtests.py

test-coverage: ## Run the tests while generating test coverage data.
	coverage run ./runtests.py && coverage report && coverage html

test-ci: ## Continuous integration test suite.
	tox

clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

publish: ## Publishes a new version to pypi.
	rm dist/* && python setup.py sdist && twine upload dist/* && echo 'Success! Go to https://pypi.python.org/pypi/wagtail-django-recaptcha and check that all is well.'
