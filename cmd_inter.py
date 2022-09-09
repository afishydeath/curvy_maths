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

def get_points(func,*args):
	match func:
		case _:
			print('invalid function')

def render(**kwargs):
	frames=100
	start_points_in=False
	name='frame'
	chaos=False
	if 'frames' in kwargs:
		frames=kwargs{'frames'}

	if 'start_points_in' in kwargs:
		start_points_in=kwargs{'start_points_in'}

	if 'name' in kwargs:
		name=kwargs{'name'}

	if 'chaos' in kwargs:
		chaos=kwargs{'chaos'}

	bezier_render.external_run(frames,start_points_in=start_points_in,name=name,chaos=chaos)
