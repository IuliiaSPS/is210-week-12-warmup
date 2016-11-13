#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Custom error class."""
    pass


def get_age(birthyear):
    """Function to count age."""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    return age
