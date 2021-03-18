#!/usr/bin/env python3

import socket, sys, os

def auth(name):
    folder = "twitch-chat-utils/" + name
    if 'XDG_CONFIG_HOME' in os.environ:
        loc = os.path.join(os.environ['XDG_CONFIG_HOME'], folder)
    else:
        loc = os.path.join(os.environ['HOME'], '.config', folder)
    with open(loc, 'r') as f:
        return f.read() 

def send(chan, name, msg, oauth):
    HOST = "irc.twitch.tv"
    PORT = 6667
    CHAN = "#" + sys.argv[1].lower()
    NICK = name
    AUTH = "oauth:" + oauth

    s = socket.socket()

    s.connect((HOST, PORT))
    s.send(str.encode("PASS " + AUTH + "\r\n"))
    s.send(str.encode("NICK " + NICK + "\r\n"))
    s.send(str.encode("JOIN " + CHAN + "\r\n"))

    msg = str.encode("PRIVMSG " + CHAN + " :" + msg + "\r\n")
    s.send(msg)

    s.close()

if __name__ == '__main__':
    send(sys.argv[1], sys.argv[2], sys.argv[3], auth(sys.argv[2]))
