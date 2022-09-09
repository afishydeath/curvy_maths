# command line interface
# <--- Unfinished --->
import sys
import bezier_pat,bezier_render

args=sys.argv[1:]

def help():
	with open('help.txt','r') as f:
		for l in f:
			print(l)

def invalid():
	print('Invalid command, use -h to see the help page')

