#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginpass = 0 #counter for pass
iplist = []
#open a file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystonefile:

#loop over the file

     for line in keystonefile:
          # if this 'fail pattern' appears in the line...
          if "- - - - -] Authorization failed" in line:
             loginfail += 1
             iplist.append(line.split(" ")[-1].strip("\n"))
          # the following elif agumentation MUST be AFTER we check for a fail
          # this statement assumes the if statement above it tested false
          elif "-] Authorization failed" in line:
              loginpass += 1
          
# display the number of failed log in attempts
print("The number of failed log in attempts is", loginfail)
print("List of IP :", iplist)

# display the number of successful log in attempts
print("The number of successful log ins is", loginpass)

