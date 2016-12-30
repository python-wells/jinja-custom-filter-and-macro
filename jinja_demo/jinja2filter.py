#!/usr/bin/env python
# coding=utf-8

"""
jinja2 custom filter example
"""

from __future__ import unicode_literals


def bool_(value):
    """format a boolean value for human reading.

    """
    return "✓" if value else "❌"
