"""
This module provides the utility functions for the app
"""
from time import sleep
from collections import namedtuple


def function_to_db(*args, **kwargs):
    a = namedtuple('User', 'id fname lname')
    sleep(10)
    a.id = 1
    a.fname = 'Tommy'
    a.lname = 'Truong'
    return a
