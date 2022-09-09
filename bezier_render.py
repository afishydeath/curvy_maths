#beizers renderer
# import beizerpat.py
import sys,math,time,os
#temp points
start_points=[[0,0]]
###
###

#Params of the screen, set in setup
WIDTH=0
HEIGHT=0

#list of dictionaries of points {'x':x,'y':y,'colour':colour}
points=[]
tpoints=[]
bpoints=[]

#list of dictionaries of lines {'x0':x0,'y0':y0,'x1':x1,'y1':y1,'colour':colour}
lines=[]
tlines=[]
blines=[]


def update_progress(progress):
	barLength = 30 # Modify this to change the length of the progress bar
	status = ""
	if isinstance(progress, int):
		progress = float(progress)
	if not isinstance(progress, float):
		progress = 0
		status = "error: progress var must be float\r\n"
	if progress < 0:
		progress = 0
		status = "Halt...\r\n"
	if progress >= 1:
		progress = 1
		status = "Done...\r\n"
	block = int(round(barLength*progress))
	if 1: # set to 0 if you don't use fira code font
		text = "\rPercent: {0} {1}% {2}".format( ""*block + ""*(barLength-block), math.floor(progress*100), status)
	else:
		text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), math.floor(progress*100), status)
	sys.stdout.write(text)
	sys.stdout.flush()

def saveFrame(frame,fname='Frame'):
	# print([[point['x'],point['y']]for point in points])
	global points
	global lines

	# with open(f'C:\\Users\\Sam Hogan\\Documents\\Coding\\bezierFrames\\{fname}{frame}.html','wt') as f:
	with open(f'svg_frames/{fname}{frame}.svg','wt') as f:
		# f.write('<<!DOCTYPE html>\n<html>\n<body>\n')
		f.write(f'<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">'+'\n')
		# print(tpoints,bpoints,points)
		for l in lines[::-1]:
			x1=str((l['x0']+100))
			y1=str(HEIGHT-(l['y0']+100))
			x2=str((l['x1']+100))
			y2=str(HEIGHT-(l['y1']+100))
			c=l['colour']
			f.write(f'\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{c};stroke-width:2;"></line>'+'\n')
		for p in points[::-1]:
			x=str((p['x']+100))
			y=str(HEIGHT-(p['y']+100))
			c=p['colour']
			f.write(f'\t<circle cx="{x}" cy="{y}" r="3" fill="{c}"></circle>'+'\n')
		for l in blines[::-1]:
			x1=str((l['x0']+100))
			y1=str(HEIGHT-(l['y0']+100))
			x2=str((l['x1']+100))
			y2=str(HEIGHT-(l['y1']+100))
			c=l['colour']
			f.write(f'\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{c};stroke-width:2;"></line>'+'\n')
		for p in bpoints[::-1]:
			x=str((p['x']+100))
			y=str(HEIGHT-(p['y']+100))
			c=p['colour']
			f.write(f'\t<circle cx="{x}" cy="{y}" r="3" fill="{c}"></circle>'+'\n')
		for l in tlines[::-1]:
			x1=str((l['x0']+100))
			y1=str(HEIGHT-(l['y0']+100))
			x2=str((l['x1']+100))
			y2=str(HEIGHT-(l['y1']+100))
			c=l['colour']
			f.write(f'\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{c};stroke-width:2;"></line>'+'\n')
		# for p in tpoints[::-1]:
		# 	x=str((p['x']+100))
		# 	y=str(HEIGHT-(p['y']+100))
		# 	c=p['colour']
		# 	f.write(f'\t<circle cx="{x}" cy="{y}" r="3" fill="{c}"></circle>'+'\n')
		f.write('</svg>'+'\n')
		# f.write('</body>\n</html>')
	points=[]
	lines=[]


def makePoint(x,y,colour='rgb(0,0,0)',version=''):
	if version=='t':
		global tpoints
		tpoints.append({'x':x,'y':y,'colour':colour})
	if version=='b':
		global bpoints
		bpoints.append({'x':x,'y':y,'colour':colour})		
	else:
		global points
		points.append({'x':x,'y':y,'colour':colour})

def makeLine(x0,y0,x1,y1,colour='rgb(0,0,0)',version=''):
	if version=='t':
		global tlines
		tlines.append({'x0':x0,'y0':y0,'x1':x1,'y1':y1,'colour':colour})
	if version=='b':
		global blines
		blines.append({'x0':x0,'y0':y0,'x1':x1,'y1':y1,'colour':colour})
	else:
		global lines
		lines.append({'x0':x0,'y0':y0,'x1':x1,'y1':y1,'colour':colour})

def setup(points):
	global WIDTH
	global HEIGHT
	# print('here',points)
	maxx=0
	maxy=0
	for i,point in enumerate(points):
		if point[0]>maxx:maxx=point[0]
		if point[1]>maxy:maxy=point[1]
		makePoint(point[0],point[1],version='b')
		if i>0:
			makeLine(oldpoint[0],oldpoint[1],point[0],point[1],version='b')
		oldpoint=point
	# print(maxx)
	WIDTH=maxx+200
	HEIGHT=maxy+200

def ipoints(t,points):
	out=[]
	for i,point in enumerate(points):
		if i>0:
			out.append([oldpoint[0]+(point[0]-oldpoint[0])*t,oldpoint[1]+(point[1]-oldpoint[1])*t])
		oldpoint=point
	return out

def chaostrails(chaosold,chaosnew,hueChange):
	for key in chaosold.keys():
		for i,point in enumerate(chaosold[key]):
			makeLine(point[0],point[1],chaosnew[key][i][0],chaosnew[key][i][1],colour=f'hsl({(len(chaosold[key])-1)*hueChange},100%,50%)',version='t')

def maintrail(old,new):
	makeLine(old[0],old[1],new[0],new[1],colour='hsl(0,100%,50%)',version='t')
	makePoint(new[0],new[1],colour='hsl(0,100%,50%)',version='t')

def frame(t,points,hueChange):
	if len(points)>1:
		for i,point in enumerate(points):
			makePoint(point[0],point[1],colour=f'hsl({(len(points)-1)*hueChange},100%,50%)')
			if i>0:
				makeLine(oldpoint[0],oldpoint[1],point[0],point[1],colour=f'hsl({(len(points)-1)*hueChange},100%,50%)')
			oldpoint=point
		f=frame(t,ipoints(t,points),hueChange)
		f[str(len(points))]=points
		return f
	return {'1':points}

def run(frames,points=start_points, name='frame',chaos=False):
	setup(points)
	os.system('rm ./svg_frames/*')
	hueChange=360/len(points)
	for f in range(frames+1):
		progress=(f/frames)
		update_progress(progress)
		t=f/frames
		if not chaos:
			tree=frame(t,points,hueChange)
			new=tree['1'][0]
			if f>0:
				maintrail(new,old)
			old=new
		else:
			chaosnew=frame(t,points,hueChange)
			if f>0:
				chaostrails(chaosold,chaosnew,hueChange)
			chaosold=chaosnew
		saveFrame(f,fname=name)

def external_run(frames,points_in=False,name='frame',chaos=False):
	points=start_points
	if points_in:
		points=points_in
	run(frames,points=points,name=name,chaos=chaos)

# if __name__ == '__main__':
# 	#Start time
# 	start_time=time.time()

# 	run(60)

# 	end_time=time.time()

# 	print(f'Took {end_time-start_time} seconds')