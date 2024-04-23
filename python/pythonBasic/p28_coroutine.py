#!/usr/bin/env python

def handeler():
    print('Initalize Handeler')
    while True:
        value = (yield)
        print('Received %s' % value)

listener = handeler()
listener.__next__()
listener.send(1)
listener.send('message')