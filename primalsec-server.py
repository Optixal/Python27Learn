import socket, sys
import statuscc

LPORT = int(sys.argv[1])
s = socket.socket()
s.bind(('0.0.0.0', LPORT))
s.listen(2)
print statuscc.NEUTRAL + "Listening on port " + str(LPORT) + "..."

(client, (ip, port)) = s.accept()
print statuscc.POSITIVE + "Received connection from " + ip

greeting = statuscc.POSITIVE + "Successfully joined server!\n"
client.send(greeting)

while True:
    data = client.recv(1024)
    client.send(statuscc.NEUTRAL + "You've typed: " + data)

client.close()
s.close()