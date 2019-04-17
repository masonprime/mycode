#!/usr/bin/python3

counter = 0

#with open("keystone.common.wsgi", "r") as keyfile:
#    mylines = keyfile.readlines()
#    for line in mylines:
#        if "- - - - -] Authorization failed" in line:
#            # counter = counter + 1
#           counter += 1

# for line in open("keystone.common.wsgi"):
#    if "- - - - -] Authorization failed" in line:
#        counter = counter + 1

with open("keystone.common.wsgi") as keyfile:
    for line in keyfile:
        if "- - - - -] Authorization failed" in line:
            counter = counter + 1

print("The number of failed logins is: ", counter)


