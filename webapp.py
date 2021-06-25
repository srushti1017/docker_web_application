#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess 
import cgi



data = cgi.FieldStorage()

cmd = data.getvalue("command")

out = subprocess.getoutput("sudo " +cmd)

print(out)