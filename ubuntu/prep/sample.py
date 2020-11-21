#!/usr/bin/python3
""" This is sample code for furure testing """
# Install pytest by
# pip3 install flake8
# pip3 install -U pytest
# pip3 install coverage

# Execution
# Static test analisys
# flake8 ubuntu/prep/sample.py

# Unit tests with pythest
# pytest pytest ubuntu/prep/sample.py

# Test coverage


def plus_one(x):
    if x > 0:
        return x+1
    else:
        return x


def mypow(x):
    return x**2
