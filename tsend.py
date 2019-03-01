#!/usr/bin/env python3

import socket, sys, os, time
import cfg

def send(chan, msg, name, oauth):

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
    send(sys.argv[1], sys.argv[2], cfg.read()['name'], cfg.read()['auth'])
