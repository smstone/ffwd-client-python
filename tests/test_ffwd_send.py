import argparse
import unittest

from ffwd.ffwd_send import tag_type


class TestFFWDSend(unittest.TestCase):
    def test_tag_type(self):
        self.assertEquals(('hello', 'world'), tag_type("hello:world"))
        self.assertEquals(('hello', 'world:two'), tag_type("hello:world:two"))

        with self.assertRaises(argparse.ArgumentTypeError):
            tag_type('hello')
