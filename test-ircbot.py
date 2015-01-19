#Practice unit tests for ircbot.
import unittest
from unittest.mock import MagicMock
from ircbot import *

class TestCmd(unittest.TestCase):

    def setUp(self):
        self.sock = MagicMock()

    def test_say(self):
        self.msg = b'yadaydaya@derp PRIVMSG !say shit'
        self.assertEqual('shit', cmd(self.msg, self.sock))
    def test_time(self):
        self.msg = b'yadaydaya@derp PRIVMSG !time'
        self.assertTrue(cmd(self.msg, self.sock))
    def test_frosti(self):
        self.msg = b'yadaydaya@derp PRIVMSG !say shit'
        self.assertTrue(cmd(self.msg, self.sock))
    def test_pong(self):
        self.msg = b'yadaydaya@derp PRIVMSG PING:shit'
        self.assertTrue(pong(self.msg, self.sock))
    def test_pong_none(self):
        self.msg = b'yadaydayapongpin@dgerp PRIVMSG :shit'
        self.assertTrue(pong(self.msg, self.sock) == None)
