#!/usr/bin/env python3

hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() METHOD TO RETURN A LOWERCASE STRING
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")

        
