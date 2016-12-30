#!/usr/bin/env python
# coding=utf-8

"""
python distribute file
"""

from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name="jinja_demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Jinja2"],
    package_data={
        b'jinja_demo': [b'templates']
    },
    author="Yuanle Song",
    author_email="sylecn@gmail.com",
    maintainer="Yuanle Song",
    maintainer_email="sylecn@gmail.com",
    description="Jinja2 custom filters demo",
    long_description="Jinja2 custom filters demo",
    license="GPLv2+",
    url="",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
