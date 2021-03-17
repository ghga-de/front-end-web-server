# GHGA Front End Web Server, a Sample Production-grade Python Repository
##Introduction
### Vision for GHGA
### Purpose of this Repository



## Integrated Tools
The following sections lay out some of the tools that are integrated into this sample production-grade repository, and it
explains the reasons for using them. There are quite a few things to configure for CI/CD and a production-grade Python repository,
so links to further documentation are provided.

### Black, Flake8, and Pre-commit Hooks. 
In the root directory, you will see several configuration files: 
*  .flake8
*  .pre-commit-config.yaml
*  pyproject.toml

These three files configure flake8, pre-commit hooks, and Black, respectively. Flake8 is a wrapper
around a bunch of Python linters. Black is an opinionated auto-formatting tool for Python that tries to 
bring the code repository into compliance with the formatting specified in pep8 (and encorced by Flake8).

You can run black and flake8 as Git pre-commit hooks locally. Make sure you have your virtual environment 
in your .gitignore file, or running black and flake8 is going to be one wild ride. If you want to see more 
documentation on these tools, check out:

[Setting up your project with pre-commit, black, and flake8](https://dev.to/m1yag1/how-to-setup-your-project-with-pre-commit-black-and-flake8-183k)

### Read the Docs and Sphinx-apidoc
Sphinx is a massive, Python-based documentation tool. In full, it is documented [here](https://www.sphinx-doc.org/en/master/index.html).

The relevant pieces of Sphinx are [sphinx-quickstart](https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html) and [sphinx-apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html).
The sphinx-quickstart tool will set up a repository for documentation by the sphinx autodoc tool. To ensure that the autodoc tool
is enabled, when you run sphinx-quickstart, run it with the --ext-autodoc extension:

`sphinx-quickstart --ext-autodoc`

For more information, see the sphinx-quickstart documentation linked above or take a look at, for example, [this tutorial](https://www.simonho.ca/programming/automatic-python-documentation/),
but be cautioned that it's using a previous version of sphinx-quickstart where the script used to ask if you wanted to enable autodocs
rather than the user having to specify it on the command line. 

The sphinx-apidoc tool is actually the justification for using Sphinx in a code repository. The tool works with autodoc to convert
docstrings in your Python code into html that can be ported over to a ReadTheDocs webpage, allowing instant documentation of your code. 
This practice also allows the developers of a repository to place code and usage examples inside their documentation and integrate that
with the docstrings. It's pretty darned sweet if you like having well-documented code. I highly recommend re-compiling the docs automatically
when code is pushed to ensure the documentation of the API is up to date. That will save your user base some headache and also lead to far
fewer emails for you... not to mention fewer curses against your name, voo doo effigies of yourself, etc.

