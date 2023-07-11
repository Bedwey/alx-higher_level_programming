#!/usr/bin/python3
import json

"""
Author: Bedwey
Date: 11/7/2023
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized.

    Returns:
        A string containing the JSON representation of the object.
    """
    return json.dumps(my_obj)
