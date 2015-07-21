# -*- coding : utf-8 -*-

import telnetlib

HOST = "192.168.68.150"
user = "hyf"
password = "123"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("ls\n")
tn.write("rm -rf hyf/SHELL\n")
tn.write("mkdir -p hyf/SHELL\n")
tn.write("cd hyf \n")
tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
tn.close()
