#!/usr/bin/python3
""" This is sample code for furure testing """
# Install pytest by
# pip install flake8
# pip install -U pytest
# pip install coverage

# Execution
# Static test analisys
# flake8 .\ubuntu\prep\sample.py

# Unit tests with pythest
# pytest .\ubuntu\prep\sample.py

# Test coverage


def plus_one(x):
    return x+1


def mypow(x):
    return x**2


def test_one():
    assert plus_one(5) == 6


def test_two():
    assert plus_one(3) == 4


def test_three():
    assert mypow(3) == 9
