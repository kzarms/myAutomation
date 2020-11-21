#!/usr/bin/python3
""" This is testing module for sample functions """
from sample import *


def test_one():
    assert plus_one(5) == 6
    assert plus_one(6) == 7
    assert plus_one(7) == 6


def test_mypow():
    ''' Add sample tests for my power '''
    assert mypow(3) == 9
    assert mypow(4) == 16
    assert mypow(2) == 8
