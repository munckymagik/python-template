# Template Python project

## Adapting the template

1. Optionally adjust `python_version` in the `[requires]` section of the `Pipfile` to match
   the version of Python you are using

## Set up

1. Install [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
2. Run `pipenv install --dev` to install project and development dependencies

## Run the tests

Testing is supported using [pytest](https://docs.pytest.org/en/latest/).

To run all tests:

```shell
$ pipenv run tests
```

## Run the executable

```shell
$ pipenv run exe
```

## Formatting

Code formatting is provided by [autopep8](https://pypi.org/project/autopep8/).

To check formatting for all files:

```shell
$ pipenv run format-check
```

To fix formatting in-place for all files:

```shell
$ pipenv run format
```

## Run the linter

Linting is provided by [pylint](http://pylint.pycqa.org/en/latest/index.html).

Run the linter using:

```shell
$ pipenv run lint
```
