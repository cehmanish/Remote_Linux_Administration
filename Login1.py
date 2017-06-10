#!/usr/bin/python
import cgi
import cgitb
import threading
import paramiko
import subprocess


form=cgi.FieldStorage()
Linux_ip=form.getvalue('ip_address')
user_name=form.getvalue('user_name')
passwd=form.getvalue('password')



reply="None"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
	client.connect(Linux_ip, username=user_name, password=passwd)
	ssh_session = client.get_transport().open_session()

#if ssh_session.active:

        reply= "Authentication Sucessfull<a href='/cgi-bin/Home.py' >Home</a>"

except:
	reply="User Name or Password Is Incorrect"
     

print "Set-Cookie:IP=%s;" %(Linux_ip)
print "Set-Cookie:USER=%s;" %(user_name)
print "Set-Cookie:PASS=%s;" %(passwd)
print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print "<p> Command Result:  %s </p>" %(reply) 
print '</body>'
print '</html>'