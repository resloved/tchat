#!/usr/bin/env python3

import os, sys

file = "twitch-utils/.config"

def folder():
    if 'APPDATA' in os.environ:
        return os.environ['APPDATA']
    if 'XDG_CONFIG_HOME' in os.environ:
        return os.environ['XDG_CONFIG_HOME']
    else:
        return os.path.join(os.environ['HOME'], '.config')

def loc():
    return os.path.join(folder(), file)

def read():
    settings = {}
    with open(loc(), 'r') as f:
        for line in f.readlines():
            split = line.split("=")
            if len(split) > 1:
                settings[split[0]] = "=".join(split[1:]).strip()
    return settings 
        
def write(add):
    new = read()
    new.update(add)
    with open(loc(), 'w') as f:
        for key, value in new.items():
            f.write(key + "=" + value)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        write({ sys.argv[1] : sys.argv[2] })
    elif len(sys.argv) == 2:
        print(read()[sys.argv[1]])
    else:
        print(read())
