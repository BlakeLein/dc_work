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
	input()


class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32


if __name__ == '__main__':
    for i in dir(Colors):
        if i[0:1] != "_" and i != "END":
            print("{:>16} {}".format(i, getattr(Colors, i) + i + Colors.END))