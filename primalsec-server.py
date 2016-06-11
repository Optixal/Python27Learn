import socket, sys
import coloredstatus as cs

LPORT = int(sys.argv[1])
s = socket.socket()
s.bind(('0.0.0.0', LPORT))
s.listen(2)
print cs.status + "Listening on port " + str(LPORT) + "..."

(client, (ip, port)) = s.accept()
print cs.good + "Received connection from " + ip

greeting = cs.good + "Successfully joined server!\n"
client.send(greeting)

while True:
    data = client.recv(1024)
    client.send(cs.status + "You've typed: " + data)

client.close()
s.close()