#!/usr/bin/python
import cgi
import cgitb
 
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Remotely Linux Administration</title>'
print '</head>'
print '<body>'
print '<h2>Remotely Linux Administration Home Page  </h2>'
print '<p>Chose Option What You Want to do On Remote Machine</p>'
print '<form action="/cgi-bin/Home1.py" method="get">'
print '<p><input name="command" type="radio" value="id">Remote Machine Information </p>'
print '<p><input name="command" type="radio" value="ls">List of File ana Folder on Remote Machine</p>'
print '<p><input name="command" type="radio" value="ifconfig">Network Configuration of Remote Machine</p>'
print '<p><input name="command" type="radio" value="who">No of Active User on Remote Machine</p>'
print '<p><input name="command" type="radio" value="ls -l">Check File Permission</p>'
print '<p><input name="command" type="radio" value="date">Check Date and Time on Remote Machine</p>'
print '<p><input name="command" type="radio" value="reboot">Reboot Remote Machine </p>'
print '<p><input name="command" type="radio" value="halt">Shutdown Remote Machine </p>'
print '<p><input name="command" type="radio" value="netstat -antp">Active Connection on Remote Machine</p>'
print '<p><input name="command" type="radio" value="ls -a">Show hidden File and Folders</p>'
print '<p><input name="submit" type="submit"></p>' 
print '</form>'
print '</body>'
print '</html>'