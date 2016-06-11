import socket, sys
import coloredstatus as cs

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])
s = socket.socket()
s.settimeout(1)
try:
    print cs.status + "Attempting to connect to remote host"
    s.connect((RHOST, RPORT))
    while True:
        data = s.recv(1024)
        print data
        input = raw_input()
        s.send(input)
    s.close()
except:
    print cs.error + "Failed to connect to remote host"
