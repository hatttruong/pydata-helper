"""
Implement some common regex pattern
    1. emoji
    2. URL
    3. non-ASCII characters
    4. number: normal number, money, phone
    5. time, date
    6. hashtags
    7. non-alphabet

with actions:
    - replace
    - remove
    - extract
    - remove & extract
    - replace & extract
"""

import re


PATTERNS = {
    'emoji': '',
    'url': '',
    'non-ascii': '',
    'number': '',
    'money': '',
    'phone': '',
    'email': '',
    'time': '',
    'date': '',
    'hashtags': '',
    'non-alphabet': '',
}


def replace(text, type_pattern):
    """Summary

    Args:
        text (TYPE): Description
        type_pattern (TYPE): Description
    """
    pass


def extract(text, type_pattern):
    """Summary

    Args:
        text (TYPE): Description
        type_pattern (TYPE): Description
    """
    pass


def remove_extract(text, type_pattern):
    """Summary

    Args:
        text (TYPE): Description
        type_pattern (TYPE): Description
    """
    pass


def replace_extract(text, type_pattern):
    """Summary

    Args:
        text (TYPE): Description
        type_pattern (TYPE): Description
    """
    pass
