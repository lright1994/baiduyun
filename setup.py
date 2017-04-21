#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec

__version__ = '0.1.1'
__author__ = 'mec'

from setuptools import setup

requirements = ['requests>=2.0.0', 'baidupcsapi==0.3.8']

setup(
    name='baiduyun',
    version=__version__,
    url='https://github.com/mecforlove/baiduyun/',
    license='Apache',
    author=__author__,
    author_email='mecforlove@outlook.com',
    decription='A baiduyun client for personal use',
    packages=['baiduyun'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        baiduyun=baiduyun.cli:main
    ''')
