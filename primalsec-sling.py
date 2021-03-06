#####################################
# sling.py - checks for resources   #
# and search for string in response #
#####################################

# Application: Automate the search for vulnerable web servers
# by extracting their version number from their web page

from bs4 import BeautifulSoup
from urllib import urlopen
import sys, optparse, socket
import coloredstatus as cs


def webreq(server, resources):  # Function takes in URL, and resources variable which contains the requests
    try:
        resource = []
        for item in open(resources, 'r'):  # Loop through the resource file
            resource.append(item.strip())  # Append each item in the file to the array
        for item in resource:  # Loop through the array and create a request for each item in the array
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)  # set a timeout on the socket connection
            url = server.strip() + item.strip()  # Format the url variable to store the request: "http://www.site.com/CFIDE/administrator/enter.cfm"
            request = urlopen(url)  # Make the request
            if search:  # If the "searc
                # h" variable is true (-s)
                parsed = BeautifulSoup(request.read(), "lxml")  # Parse the output with BeautifulSoup
                if search in str(parsed):  # If the search string is in the output print the next line
                    print cs.good + url + " [" + str(request.getcode()) + "] Found: '" + search + "' in ouput"
            elif request.getcode() == 404:  # If we got an HTTP status code
                print cs.error + url + " [" + str(request.getcode()) + "]"  # Print the URL and status code
            elif request.getcode():
                print cs.good + url + " [" + str(request.getcode()) + "]"

    except:pass


def main():
    # Creates CLI switches and stores in variables
    parser = optparse.OptionParser(sys.argv[0] + ' ' + \
                                   '-i <file_with URLs> -r  -s [optional]')
    parser.add_option('-i', dest='servers', type='string', help='specify target file with URLs')
    parser.add_option('-r', dest='resources', type='string', help='specify a file with resources to request')
    parser.add_option('-s', dest='search', type='string', help='[optional] Specify a search string -s ')
    (options, args) = parser.parse_args()
    servers = options.servers
    resources = options.resources
    global search
    search = options.search

    if (servers == None) and (resources == None):  # Checks to make sure proper CLI switches were given
        print parser.usage  # if not print usage
        sys.exit(0)

    if servers:
        for server in open(servers, 'r'):  # loop through each URL in the file
            webreq(server, resources)  # Invoke the webreq function


if __name__ == "__main__":
    main()