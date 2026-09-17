.PHONY: install test docs lint

install:
	python -m pip install -e '.[dev]'

test:
	python -m pytest tests/tests.py -v
	python -c 'import doctest, re; f = lambda: None; f.__doc__ = re.search(r"```python\n(.*?)\n```", open("README.md").read(), re.DOTALL).group(1); doctest.run_docstring_examples(f, globals(), verbose=True)'

docs:
	python -m pdoc bengali_romanizer -o build/docs

install-deps:
	$(MAKE) install

lint:
	python -m ruff check bengali_romanizer/ tests/
	python -m ruff format --check bengali_romanizer/ tests/
