#!/usr/bin/env python
# coding=utf-8

"""
test Jinja2 custom filters and tags
"""

from __future__ import unicode_literals

from jinja2 import Environment, PackageLoader

from .jinja2filter import bool_


env = Environment(loader=PackageLoader('jinja_demo', 'templates'),
                  autoescape=True)
env.filters.update({
    "bool_": bool_
})


def test_filter():
    assert env.get_template("filter_demo.html").render() == "✓"


def test_macro():
    assert env.get_template("macro_demo.html").render() == """\
<a href="http://www.example.com" rel="noopener noreferrer">Example&lt;1&gt;</a>"""
