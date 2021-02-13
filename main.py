#!/usr/bin/python3

import os

from autobahn.twisted.component import Component, run
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.internet import reactor


transport = {
    "type": "rawsocket",
    "url": "ws://localhost/ws",
    "endpoint": UNIXClientEndpoint(reactor, os.path.join(os.path.expandvars('$SNAP_COMMON'), 'sockdir/thinghub.sock')),
    "serializer": "cbor"
}

component = Component(transports=[transport], realm="realm1")


@component.on_join
def main(session, details):
    print("Client session={}".format(session))


if __name__ == '__main__':
    run([component])
