import os,sys
import urllib
import socket
print "use http(s)://www.site.com"
site = raw_input("enter here site: ")
info = site.find("http://")
if info == 0:
 ip = socket.gethostbyname(site[7:])
 if len(ip) == 0:
   print "ERROR try again and make sure of your site"
 else:
  print "ip of your site is : {}".format(ip)
  data = urllib.urlopen(site)
  try:
   file = open("code_web.txt", "w")
   file.write(data.read())
   print "it completed"
  except IOError:
    print "[X] ERROR :try again and make sure of your site"
else:
  ip = socket.gethostbyname(site[8:])
  print "ip of your site is : {}".format(ip)
  data = urllib.urlopen(site)
  try:
   file = open("code_web.txt", "w")
   file.write(data.read())
   print "it completed"
  except IOError:
   print "[X] ERROR :try again and make sure of your site"
