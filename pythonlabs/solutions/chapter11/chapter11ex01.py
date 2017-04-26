#!/usr/bin/env python3
#
# A Solution For Chapter 11 Exercise 1
#
import sys, os
for command in sys.argv[1:]:
	pid = os.fork()
	if pid == 0:
		os.execv("/bin/" + command, [command])
		print("error in forking ")
		exit()
	elif pid > 0:
		os.wait()
	else:
		print("error in forking\n");
