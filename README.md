# Template Python application

This is a template Python project. Use it to seed new applications.

Included features are:

* An application entry point using the [runpy](https://docs.python.org/3/library/runpy.html) / `python -m` mechanism
* Dependency and environment management using [Pipenv](https://pipenv.pypa.io/en/latest/)
* Tests using [pytest](https://docs.pytest.org/en/latest/)
* Linting using [pylint](http://pylint.pycqa.org/en/latest/index.html)
* Formatting using [autopep8](https://pypi.org/project/autopep8/)
* CI using [GitHub Actions](https://help.github.com/en/actions)
* An [EditorConfig](https://editorconfig.org/) configuration file

## Adapting the template

1. Optionally adjust `python_version` in the `[requires]` section of the `Pipfile` to match
   the version of Python you are using
2. Rename the `projname` folder to suit your real project name
3. Search and replace all occurrences of `projname` with your new project name

## Set up

1. Install [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
2. Run `pipenv install --dev` to install project and development dependencies

## Run the application

```shell
$ pipenv run app
```

## Run the tests

To run all tests:

```shell
$ pipenv run tests
```

## Formatting

To check formatting for all files:

```shell
$ pipenv run format-check
```

To fix formatting in-place for all files:

```shell
$ pipenv run format
```

## Run the linter

Run the linter using:

```shell
$ pipenv run lint
```
