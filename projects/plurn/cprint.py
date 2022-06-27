#Cool Print - Scrolls out text letter by letter, with style!
#Insert '/' in input string to add pause

import os
import time
import threading
from threading import Thread

def cprint(string):

	#Create a flag that will signal when Enter is pressed
	e = threading.Event()
	def check_for_keypress():
		input()
		e.set()

	def do_cprint(string): 
		#Print Delay in s	
		speed = 0.05

		for c in string:
			if e.is_set():
				speed = 0 #Remove delay to print rest of text
			time.sleep(speed)
			if c == '.' or c == ',':
				print(c, end = '', flush = True )
				time.sleep(speed * 8)
			elif c == '/':
				time.sleep(speed * 5)
			else:
				#Remove newline and stop python from buffering text	
				print(c, end = '', flush = True )
		print("")

	# Create thread objects for print and keypress check
	keythread = Thread(target=check_for_keypress)	
	printthread = Thread(target=do_cprint, args=(string,))

	# This will hide user input if the user hits enter
	# otherwise, the newline will break up the text 
	os.system("stty -echo")
	
	# Start both threads
	keythread.start()
	printthread.start()
	
	# Wait for print thread to complete
	printthread.join()

	# Unhide user input
	os.system("stty echo")