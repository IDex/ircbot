#Simple ircbot, practice socket usage
#TODO: commands should be in a convinient list of tuples

import socket
import time 
import datetime 

HOST = ("irc.cs.hut.fi", "6668")
NICK = "IDePY" 
USERNAME = "asd"
RNAME = "asd" 
CHANNEL = "#kartelli1"

def pong(msg, sock):
    if msg.find(b'PING') != -1:
        sock.send(b'PONG' + msg.lstrip(b'PING'))
        return True

def cmd(msg, sock):
    if msg.find(b'!') == -1:
        return None
    if msg.find(b'!say') != -1:
        say = msg.split(b'!say')[1].decode('utf-8').rstrip('\r\n').lstrip()
    elif msg.find(b'!time') != -1:
        say = time.strftime('%H:%M %a, %d.%m.')
    elif msg.find(b'!frosti') != -1:
        date = datetime.datetime(2015, 2, 13)
        say = str(date - date.now()).rsplit(':',1)[0]
    else:
        return None
    sock.send('PRIVMSG {} : {}\r\n'.format(CHANNEL,say).encode('utf-8'))
    return say

def main():
    sock = socket.create_connection(HOST)
    joinmsg = ["NICK {}\r\n".format(NICK),
                "USER {} 0 * :{}\r\n".format(USERNAME, RNAME), 
                "JOIN :{}\r\n".format(CHANNEL)]
    for msg in joinmsg:
        sock.send(bytes(msg, 'utf-8'))
        time.sleep(1)
    while True:
        msg = sock.recv(1024)
        print(msg)
        if not pong(msg, sock):
            cmd(msg, sock)

if __name__ == '__main__':
    main()
