#!/usr/bin/python

import os

class Domain:

    def __init__(self, domain, port, protocol):
        self.domain = domain
        self.port = port
        self.protocol = protocol

    def URL(self):
        URL = self.protocol + "://" + self.domain + ":" + self.port
        return URL

    def lookup(self):
        os.system("host " + self.domain)

google = Domain('google.com', '443', 'https')
print google.port
print google.URL()
google.lookup()
