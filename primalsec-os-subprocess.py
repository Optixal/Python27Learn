import subprocess


cmd_str = "echo hello"
cmd = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
(result, error) = cmd.communicate()
print result


command_string = "uname -a"
command = subprocess.Popen(command_string, shell=True, stdout=subprocess.PIPE)
(output, err) = command.communicate()

f = open('file.txt', 'w')
f.write(output)
f.close()

for line in open('file.txt', 'r'):
    print line.strip()

