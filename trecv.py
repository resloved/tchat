#!/usr/bin/env python3

import socket, sys, re

def recv(chan, msgs=None):

    HOST = "irc.twitch.tv"
    CHAN = "#" + chan
    NICK = "justinfan12345"

    s = socket.socket()

    s.connect((HOST, 6667))
    s.send(str.encode("USER " + HOST + "\r\n"))
    s.send(str.encode("NICK " + NICK + "\r\n"))
    s.send(str.encode("JOIN " + CHAN + "\r\n"))

    while True:
        r = s.recv(1024).decode("utf-8", errors="ignore").strip()
        if "PING" in r:
            s.send("PONG tmi.twitch.tv\r\n".encode("utf-8"))  
        for msg in r.split("\n"):
            if msgs:
                msgs.append(msg)
            else:
                print(msg)

if __name__ == '__main__':
    recv(sys.argv[1])
