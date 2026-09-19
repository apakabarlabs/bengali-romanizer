.DEFAULT_GOAL := build

.PHONY: install install-tools build test docs comments lint format wheel-smoke clean

COMMENTCENSOR_VERSION ?= v0.3.2
COMMENTCENSOR_ENV = .tools/commentcensor
COMMENTCENSOR = $(COMMENTCENSOR_ENV)/bin/commentcensor

install:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip setuptools
	venv/bin/pip install -e '.[dev]'

install-tools:
	python3 -m venv $(COMMENTCENSOR_ENV)
	$(COMMENTCENSOR_ENV)/bin/pip install --quiet --upgrade git+https://github.com/botforge-pro/commentcensor.git@$(COMMENTCENSOR_VERSION)

test:
	venv/bin/pytest --cov --cov-report=term-missing --doctest-glob=README.md README.md tests

docs:
	venv/bin/python -m pdoc bengali_romanizer -o build/docs

install-deps:
	$(MAKE) install

comments:
	$(COMMENTCENSOR) .

lint: comments
	venv/bin/python -m ruff check bengali_romanizer tests
	venv/bin/python -m ruff format --check bengali_romanizer tests
	venv/bin/mypy bengali_romanizer tests

format:
	venv/bin/python -m ruff check --fix bengali_romanizer tests
	venv/bin/python -m ruff format bengali_romanizer tests

build: lint test docs
	venv/bin/python -m build
	venv/bin/python -m twine check dist/*

wheel-smoke:
	rm -rf build dist
	venv/bin/python -m build --wheel --no-isolation
	rm -rf /tmp/bengali-romanizer-smoke
	python3 -m venv /tmp/bengali-romanizer-smoke
	/tmp/bengali-romanizer-smoke/bin/pip install dist/*.whl
	/tmp/bengali-romanizer-smoke/bin/python -c "import bengali_romanizer; assert bengali_romanizer.__version__ == '0.2.0'; assert bengali_romanizer.romanize('বাংলা') == 'bangla'"
	rm -rf /tmp/bengali-romanizer-smoke

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
