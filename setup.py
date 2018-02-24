import os
import unittest

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name = "dixi",
    version = "0.0.1",
    author = "Thijs Vogels",
    author_email = "t.vogels@me.com",
    description = ("Wrapper around Python dicts that makes it easy to deal with nested tree structures."),
    license = "BSD",
    keywords = "dict, tree, numpy slicing",
    url = "https://github.com/tvogels/pyexr",
    packages=['dixi'],
    long_description=read('README.md'),
    test_suite='setup.test_suite',
)
