import socket

network = '192.168.137.'
range = range(135, 141)
hosts = []
for octet in range:
    hosts.append(network + str(octet))
ports = [21, 22, 80, 443]

for host in hosts:
    print "[*] Scanning " + host + ":"
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, port))
            s.send("\x41\r\n")
            banner = s.recv(3)
            if banner:
                print "[+] Port " + str(port) + " is open"
            s.close()
        except:
            print "[-] Unable to connect"