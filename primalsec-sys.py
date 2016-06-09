import sys

if len(sys.argv) < 3:
    print "[-] Missing input"
    exit(1)

script = sys.argv[0]
ip = sys.argv[1]
port = sys.argv[2]

print "[*] The script name is " + script
print "[*] The IP is " + ip + " and the port is " + port
