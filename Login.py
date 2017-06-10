#!/usr/bin/python
import cgi
import cgitb
 
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print '</head>'
print '<body>'
print '<h2>Welcome to Remotely Linux Administration Services Login Portel </h2>'
print '<form action="/cgi-bin/Login1.py" method="get">'
print '<p>Linux IP Address:<input name="ip_address" type="name" ></p>'
print '<p>SSH User Name:<input name="user_name" type="name"> </p>'
print '<p>SSH Password:<input name="password" type="password"></p>'
print '<p><input name="submit" type="submit"></p>' 
print '</form>'
print '<h3>Not Register!!!<a href="/cgi-bin/register.py" />Register</a> </h3>'
print '</body>'
print '</html>'