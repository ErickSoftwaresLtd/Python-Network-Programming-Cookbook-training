#!/usr/bin/env python2
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modification.

import argparse
import httplib

REMOTE_SERVER_HOST = 'www.python.org'
REMOTE_SERVER_PATH = '/'

class HTTPClient:
    def __init__(self, host):
        self.host = host

    def fetch(self, path):
        http = httplib.HTTP(self.host)

        # Prepare header
        http.putrequest("GET", path)
        http.putheader("User-Agent", __file__)
        http.putheader("HOST", self.host)
        http.putheader("Accept", "*/*")
        http.endheaders()

        try:
            errcode, errmsg, headers = http.getreply()
        except Exception, e:
            print "Client failed error code: %s message:%s headers:%s" % (errorcode, errmsg, headers)
        else:
            print "Got homepage from %s" % self.host

        file = http.getfile()
        return file.read()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host", default=REMOTE_SERVER_HOST)
    parser.add_argument('--path', action="store", dest="path", default=REMOTE_SERVER_PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print client.fetch(path)
