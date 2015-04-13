import unittest
from webassets import Bundle, Environment
from webassets_react import React
from os import path

class ReactFilterTestCase(unittest.TestCase):
    def test_output(self):
        environment = Environment(path.dirname(__file__))
        bundle = Bundle('input.jsx', output='input.js', filters=('react',))
        environment.register('test_bundle', bundle)
        bundle.build()

