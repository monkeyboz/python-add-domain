#!/usr/bin/python

# This script will be used to allow a user to create their own domains on the server. 
# It allows the average user the ability to make the right choices easily without needing to remember every small detail.
# It is currently very basic, but I will be placing more optons later on down the line. Hoping to have things lined up in a few days.
#-------------------------------------------------------
import subprocess
import re

#read in the domain name that will be used for the system. 
#This works great in setting up new domains and hosted information on the server
#--------------------------------------------------------
print "enter new domain name"
domain = raw_input()

#double checking to make sure subprocess exists on server
#--------------------------------------------------------
return_code =  subprocess.call("echo " + domain, shell=True)

print "Writing domain files to apache"
#subprocess.call("sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/" + domain, shell=True)
subprocess.call("sudo mkdir /var/www/html/"+domain, shell=True)

try:
	myfile = open("template.conf")
except IOError:
	print "File is not available"

#opens the main default domain file which is used for setting up basic domain structures
#--------------------------------------------------------
info_holder = ""

#function used to read in line and concat information to the line
#--------------------------------------------------------
def getLine(line,domain):
	info = ["ServerName","DocumentRoot","hosted_file_directory"]
	for i in info: 
		result = re.search("\W+"+i+'\W+',line)
		if result:
			if i == "DocumentRoot":
				line = "\t"+i+" /var/www/html/"+domain+"\r\n"
			if i == "hosted_file_directory":
				line = "<Directory /var/www/html/"+domain+">\r\n"
			if i == "ServerName":
				line = "\t"+i+" "+domain+"\r\n"
			
	return line

#looping through function create lines needed for domain file
#----------------------------------------------------------
for line in myfile:
	line = getLine(line,domain)
	info_holder += line

print info_holder

#subprocess.call("sudo echo "+info_holder+" > /etc/apache2/sites-available/"+domain+".conf", shell=True)

try: 
	newdomain = open("/etc/apache2/sites-available/"+domain+".conf", "w+")
	newdomain.write(info_holder)
except IOError:
	print "File is not available"

#enables the domain on the apache server
#----------------------------------------------------------
print "Enabling domain in apache"
subprocess.call("sudo a2ensite " + domain, shell=True)

#restarts the apache server
#----------------------------------------------------------
print "Restarting apache"
subprocess.call("sudo /etc/init.d/apache2 restart", shell=True)

#edits the host file to make sure that the domain in available on the server
#open("/etc/hosts").write("\r\nlocalhost		"+domain)
#subprocess.call("sudo echo "+domain+" localhost > /etc/hosts", shell=True)

test_domain = open("/etc/hosts");

print "\r\n\r\n\r\nDomains that are currently available"
for line in test_domain:
	print line

print "Add this line by hand to your host file \r\n"
print "127.0.0.1 \t"+domain

#call(["echo testing","-l"])
