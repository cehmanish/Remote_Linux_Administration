#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
 
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print '</head>'
print '<body>'
print '<h2>Welcome to Remotely Linux Administration Services Registration Page </h2>'
print '<h6>Send Your Details to admin@myhacker.online</h6>'
print '<p>Already Registered !!!<a href="/cgi-bin/Login.py" /> Login</a></p>'
print '</body>'
print '</html>'
