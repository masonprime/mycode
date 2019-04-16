#!/usr/bin/python3

import urllib.request
import json

def main ():
	majortom = urllib.request.urlopen('http://api.open-notify.org/astros.json')

	helmetson = majortom.read().decode('utf-8')

	groundctrl = json.loads(helmetson)
	
	## I'm trying to loop across groundcrtl and I just need to display the names

	for astro in groundctrl['people']:
		print(astro['name'])


	# print(majortom.headers)

	# print(type(majortom))

	# print(dir(majortom))

	input('press enter to exit')
	
main()
# main() runs the c ode each time it appears
main()
                      
