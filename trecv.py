#!/usr/bin/env python3

import socket, sys, re

def recv(chan):
    HOST = "irc.twitch.tv"
    CHAN = "#" + chan
    NICK = "justinfan12345"

    s = socket.socket()

    s.connect((HOST, 6667))
    s.send(str.encode("USER " + HOST + "\r\n"))
    s.send(str.encode("NICK " + NICK + "\r\n"))
    s.send(str.encode("JOIN " + CHAN + "\r\n"))

    while True:
        r = s.recv(1024).decode("utf-8", errors="ignore")
        if "PING" in r:
            s.send("PONG tmi.twitch.tv\r\n".encode("utf-8"))  
        for msg in r.split("\n"):
            if "PRIVMSG" in msg:
                print(parse(msg), flush=True)

def parse(raw):
    regex = r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :"
    usr = re.search(r"\w+", raw).group(0)
    txt = re.compile(regex).sub("", raw)
    return usr + " " + txt

if __name__ == '__main__':
    recv(sys.argv[1])
