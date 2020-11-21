# Simple examples
Example files

## Installing prereq

Install modules


```
pip3 install flake8
pip3 install -U pytest
pip3 install coverage
```

## Tesing process
Example for tests

Static code analysis, unit tests and code coverage
```
flake8 ubuntu/prep/sample.py
pytest ubuntu/prep/test_sample.py
# Coverage
coverage run -m pytest ubuntu/prep/test_sample.py
coverage report -m
coverage erase
```