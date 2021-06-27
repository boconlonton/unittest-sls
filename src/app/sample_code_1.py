"""
This is a docstring
"""
from utils import function_to_db


def validate():
    return True


def helper_func1():
    pass


def helper_func2():
    pass


def handler(event, context):
    if validate():
        helper_func1()
        helper_func2()
        query = 'SELECT * FROM user WHERE id = 1'
        usr_obj = function_to_db(query)
    return usr_obj
