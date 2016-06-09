#!/usr/bin/python

POSITIVE = "\033[1m\033[92m[+]\033[0m "
NEGATIVE = "\033[1m\033[91m[-]\033[0m "
NEUTRAL = "\033[1m\033[94m[*]\033[0m "

MONEY = "\033[1m\033[92m[$]\033[0m "
WARNING = "\033[1m\033[93m[!]\033[0m "
SPECIAL = "\033[1m\033[38;5;198m[#]\033[0m "

def main():
    print POSITIVE + "Password hash dumped!"
    print NEGATIVE + "Failed to connect to host"
    print NEUTRAL + "Scanning for host...\n"
    print MONEY + "Jackpot!"
    print WARNING + "Dangerous!"
    print SPECIAL + "Administrative privileges granted"

if __name__ == "__main__":
    main()