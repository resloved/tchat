#!/usr/bin/env python3

import socket, sys, os

def settings():
    
    settings = {}
    file = "twitch-utils/.config"
    
    if 'XDG_CONFIG_HOME' in os.environ:
        loc = os.path.join(os.environ['XDG_CONFIG_HOME'], file)
    else:
        loc = os.path.join(os.environ['HOME'], '.config', file)

    with open(loc, 'r') as f:
        for line in f.readlines():
            split = line.split("=")
            if len(split) > 1:
                settings[split[0]] = "=".join(split[1:]).strip()

    return settings

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
    secret = settings()
    send(sys.argv[1], sys.argv[2], secret['name'], secret['auth'])
