#!/usr/bin/python
import cgi
import cgitb
 
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print '</head>'
print '<body>'
print '<h2>Welcome to Remotely Linux Administration Services </h2>'
print '<h3><a href="/cgi-bin/Login.py" /> Login</a></h3>'
print '<h3><a href="/cgi-bin/Register.py" />Register</a> </h3>'
print '</body>'
print '</html>'
