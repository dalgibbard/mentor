#!/usr/bin/env python

from distutils.core import setup

setup(name='mentor',
    version="0.1",
    description='Simple file sharing tool over HTTP',
    author='fim',
    install_requires=[
        'gevent'],
#    author_email='',
    scripts=['mentor']
)
