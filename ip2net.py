#!/usr/bin/env python
import sys, os, optparse
from cymruwhois import Client


def look(iplist):
    c = Client()  # creates an instance of the Client class
    try:
        if ips != None:
            r = c.lookupmany_dict(iplist)  # leverages the lookupmany_dict() function to pass in a list of IPs
            for ip in iplist:  # Iterates over the ips in the list to use a key value in the dictionary from lookupman_dict()
                net = r[ip].prefix;
                owner = r[ip].owner;
                cc = r[ip].cc  # gets the networking information from the dictionary
                line = '%-20s # - %15s (%s) - %s' % (net, ip, cc, owner)  # formats the line to print cleanly
                print line
    except:pass


def checkFile(ips):  # Checks to ensure the file can be read
    if not os.path.isfile(ips):
        print '[-] ' + ips + ' does not exist.'
        sys.exit(0)
    if not os.access(ips, os.R_OK):
        print '[-] ' + ips + ' access denied.'
        sys.exit(0)
    print '[+] Querying from:  ' + ips


def main():
    parser = optparse.OptionParser('%prog ' + \
                                   '-r <file_with IPs> || -i <IP>')
    parser.add_option('-r', dest='ips', type='string', \
                      help='specify target file with IPs')
    parser.add_option('-i', dest='ip', type='string', \
                      help='specify a target IP address')
    (options, args) = parser.parse_args()
    ip = options.ip  # Assigns a -i <IP> to variable 'ip'
    global ips;
    ips = options.ips  # Assigns a -r <fileName> to variable 'ips'
    if (ips == None) and (ip == None):  # If proper arguments aren't given print the script usage
        print parser.usage
        sys.exit(0)
    if ips != None:  # Execute if ips has a value
        checkFile(ips)  # Execute the function to check if the file can be read
        iplist = []  # create the ipslist list object
        for line in open(ips, 'r'):  # Parse File to create a list
            iplist.append(line.strip('\n'))  # Appends that line in the file to list and removes the new line char
        look(iplist)  # pass the iplist list object to the look() function

    else:  # Executes lookup() function for a single IP stored in variable 'ip'
        try:
            c = Client()
            r = c.lookup(ip)
            net = r.prefix;
            owner = r.owner;
            cc = r.cc
            line = '%-20s # - %15s (%s) - %s' % (net, ip, cc, owner)
            print line
        except:pass

if __name__ == "__main__":
    main()