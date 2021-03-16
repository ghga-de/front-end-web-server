# GHGA Front End Web Server
### Or: A sample production-grade Python repository

### Black, Flake8, and Pre-commit Hooks. 
In the root directory, you will see several configuration files: 
*  .flake8
*  .pre-commit-config.yaml
*  pyproject.toml

These three files configure flake8, pre-commit hooks, and Black, respectively. Flake8 is a wrapper
around a bunch of Python linters. Black is an opinionated auto-formatting tool for Python that tries to 
bring the code repository into compliance with the formatting specified in pep8 (and encorced in Flake8).

You can run black and flake8 as Git pre-commit hooks locally. Make sure you have your virtual environment 
in your .gitignore file, or that's going to be one wild ride. 