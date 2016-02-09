#Practice unit tests for ircbot.
import unittest
import datetime 
import time
from unittest.mock import MagicMock
from ircbot import *

class TestCmd(unittest.TestCase):

    def setUp(self):
        self.sock = MagicMock()

    def test_say(self):
        self.msg = b'yadaydaya@derp PRIVMSG !say shit'
        assert('shit' == cmd(self.msg, self.sock))
    def test_time(self):
        self.msg = b'yadaydaya@derp PRIVMSG !time'
        say = time.strftime('%H:%M %a, %d.%m.')
        self.assertTrue(cmd(self.msg, self.sock) == say)
    def test_frosti(self):
        self.msg = b'yadaydaya@derp PRIVMSG !frosti shit'
        date = datetime.datetime(2015, 2, 13)
        say = str(date - date.now()).rsplit(':',1)[0]
        self.assertTrue(cmd(self.msg, self.sock) == say)
    def test_chan(self):
        self.msg = b'IDe!itajar@derp PRIVMSG !chan #shit'
        say = '#shit'
        print(cmd(self.msg, self.sock))
        self.assertTrue(cmd(self.msg, self.sock) == say)
    def test_pong(self):
        self.msg = b'yadaydaya@derp PRIVMSG PING:shit'
        self.assertTrue(pong(self.msg, self.sock))
    def test_pong_none(self):
        self.msg = b'yadaydayapongpin@dgerp PRIVMSG :shit'
        self.assertTrue(pong(self.msg, self.sock) == None)
