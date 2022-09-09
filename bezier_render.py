#beizers renderer
# import beizerpat.py
import sys,math,time,os
#temp points
start_points=[[0, 0.0], [0.0, 500], [500, 500.0], [500.0, 0], [0, 10.0], [500, 490.0], [0, 10.0], [490.0, 0], [500, 480.0], [20.0, 500], [0, 20.0], [480.0, 0], [0, 30.0], [30.0, 500], [500, 470.0], [470.0, 0], [0, 40.0], [500, 460.0], [0, 40.0], [460.0, 0], [500, 450.0], [50.0, 500], [0, 50.0], [450.0, 0], [0, 60.0], [60.0, 500], [500, 440.0], [440.0, 0], [0, 70.0], [500, 430.0], [0, 70.0], [430.0, 0], [500, 420.0], [80.0, 500], [0, 80.0], [420.0, 0], [0, 90.0], [90.0, 500], [500, 410.0], [410.0, 0], [0, 100.0], [500, 400.0], [0, 100.0], [400.0, 0], [500, 390.0], [110.0, 500], [0, 110.0], [390.0, 0], [0, 120.0], [120.0, 500], [500, 380.0], [380.0, 0], [0, 130.0], [500, 370.0], [0, 130.0], [370.0, 0], [500, 360.0], [140.0, 500], [0, 140.0], [360.0, 0], [0, 150.0], [150.0, 500], [500, 350.0], [350.0, 0], [0, 160.0], [500, 340.0], [0, 160.0], [340.0, 0], [500, 330.0], [170.0, 500], [0, 170.0], [330.0, 0], [0, 180.0], [180.0, 500], [500, 320.0], [320.0, 0], [0, 190.0], [500, 310.0], [0, 190.0], [310.0, 0], [500, 300.0], [200.0, 500], [0, 200.0], [300.0, 0], [0, 210.0], [210.0, 500], [500, 290.0], [290.0, 0], [0, 220.0], [500, 280.0], [0, 220.0], [280.0, 0], [500, 270.0], [230.0, 500], [0, 230.0], [270.0, 0], [0, 240.0], [240.0, 500], [500, 260.0], [260.0, 0], [0, 250.0], [500, 250.0], [0, 250.0], [250.0, 0], [500, 240.0], [260.0, 500], [0, 260.0], [240.0, 0], [0, 270.0], [270.0, 500], [500, 230.0], [230.0, 0], [0, 280.0], [500, 220.0], [0, 280.0], [220.0, 0], [500, 210.0], [290.0, 500], [0, 290.0], [210.0, 0], [0, 300.0], [300.0, 500], [500, 200.0], [200.0, 0], [0, 310.0], [500, 190.0], [0, 310.0], [190.0, 0], [500, 180.0], [320.0, 500], [0, 320.0], [180.0, 0], [0, 330.0], [330.0, 500], [500, 170.0], [170.0, 0], [0, 340.0], [500, 160.0], [0, 340.0], [160.0, 0], [500, 150.0], [350.0, 500], [0, 350.0], [150.0, 0], [0, 360.0], [360.0, 500], [500, 140.0], [140.0, 0], [0, 370.0], [500, 130.0], [0, 370.0], [130.0, 0], [500, 120.0], [380.0, 500], [0, 380.0], [120.0, 0], [0, 390.0], [390.0, 500], [500, 110.0], [110.0, 0], [0, 400.0], [500, 100.0], [0, 400.0], [100.0, 0], [500, 90.0], [410.0, 500], [0, 410.0], [90.0, 0], [0, 420.0], [420.0, 500], [500, 80.0], [80.0, 0], [0, 430.0], [500, 70.0], [0, 430.0], [70.0, 0], [500, 60.0], [440.0, 500], [0, 440.0], [60.0, 0], [0, 450.0], [450.0, 500], [500, 50.0], [50.0, 0], [0, 460.0], [500, 40.0], [0, 460.0], [40.0, 0], [500, 30.0], [470.0, 500], [0, 470.0], [30.0, 0], [0, 480.0], [480.0, 500], [500, 20.0], [20.0, 0], [0, 490.0], [500, 10.0], [0, 490.0], [10.0, 0]]
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

def run(frames,name='frame',chaos=False):
	setup(start_points)
	os.system('rm ./svg_frames/*')
	hueChange=360/len(start_points)
	for f in range(frames+1):
		progress=(f/frames)
		update_progress(progress)
		t=f/frames
		if not chaos:
			tree=frame(t,start_points,hueChange)
			new=tree['1'][0]
			if f>0:
				maintrail(new,old)
			old=new
		else:
			chaosnew=frame(t,start_points,hueChange)
			if f>0:
				chaostrails(chaosold,chaosnew,hueChange)
			chaosold=chaosnew
		saveFrame(f,fname=name)

def external_run(frames,start_points_in=False,name='frame',chaos=False):
	if start_points_in:
		global start_points
		start_points=start_points_in
	run(frames,name=name,chaos=chaos)

# if __name__ == '__main__':
# 	#Start time
# 	start_time=time.time()

# 	run(60)

# 	end_time=time.time()

# 	print(f'Took {end_time-start_time} seconds')