#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import threading
import paramiko
import subprocess
from os import environ 
import string 

Linux_ip=""
user_name=""
passwd=""

if environ.has_key('HTTP_COOKIE'):
	for cookie in map(string.strip,string.split(environ['HTTP_COOKIE'],';')):
		(key,value)=string.split(cookie, '=');
		if key == "IP":
			Linux_ip=value
		if key =="USER":
			user_name=value
		if key == "PASS":
			passwd=value


form=cgi.FieldStorage()
command=form.getvalue('command')
reply="None"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:

	client.connect(Linux_ip, username=user_name, password=passwd)
	ssh_session = client.get_transport().open_session()

	if ssh_session.active:
	
        	ssh_session.exec_command(command)
		reply=ssh_session.recv(1024)

except:
	reply="Unable to Connect Remote Machine"
    
 
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print '<body>'
print '<h3>Response From Remote Linux Machine </h3>'
print "<p> Result:  %s </p>" %(reply) 
print '<p><a href="/cgi-bin/Home.py" > Home</p>'
print '</body>'
print '</html>'