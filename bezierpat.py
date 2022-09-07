#patterns for bezier
import math
def zig_zag(step,size,mult):
	out=[[i*step,0] if i%2==0 else [(i-1)*step+step,size] for i in range(mult*2)]
	return out

def sin_points(step,size,mult):
	out=[[i*step,size+int(math.sin(math.radians(i*step)*size))] for i in range(360*mult//step+1)]
	return out

def make_curve(step,size):
	out=[[0,i//2*step] if i%2==0 else [(i//2+1)*step,size] for i in range((size//step)*2)]
	return out

def full_size_v(w,h,step):
	out=[[0,i//2*step] if i%2==0 else [w,h-i//2*step] for i in range((h//step+1)*2)]
	return out

def full_size_h(w,h,step):
	out=[[i//2*step,0] if i%2==0 else [w-i//2*step,h] for i in range((h//step+1)*2)]
	return out

def diamond(w,h,iters):
	out=[[w-(i//4*(w/iters)),0] if (i+1)%4==0 else([w,h-(i//4*(h/iters))] if (i+1)%3==0 else ([i//4*(w/iters),h] if (i+1)%2==0 else [0,i//4*(h/iters)])) for i in range(iters*4)]
	return out

def spiral(iters,size=100):
	if iters==0:
		return [0,0]
	out = [[sum([(-1 if j%4==3 else 1)*math.ceil(j/2)*size/((iters-2)//4+1) for j in range(1,i+1,2)]),sum([(-1 if j%4==2 else 1)*math.ceil(j/2)*size/((iters-2)//4+1) for j in range(0,i+1,2)])] for i in range(iters)]
	return out


def rightHorizNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x0+((x1-x0)/4),y0+math.tan(math.radians(60))*((x1-x0)/4)]
	p3=[x1-((x1-x0)/4),y0+math.tan(math.radians(60))*((x1-x0)/4)]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def leftHorizNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x0+((x1-x0)/4),y0+math.tan(math.radians(60))*((x0-x1)/4)]
	p3=[x1-((x1-x0)/4),y0+math.tan(math.radians(60))*((x0-x1)/4)]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def upRightNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x1,y0]
	p3=[x1+(x1-x0)/2,y0+(y1-y0)/2]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def downLeftNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x0+(x0-x1)/2,y1+(y0-y1)/2]
	p3=[x0,y1]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def upLeftNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x1,y0]
	p3=[x1-(x0-x1)/2,y0+(y1-y0)/2]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def downRightNL(x0,y0,x1,y1):
	p1=[x0,y0]
	p2=[x0-(x1-x0)/2,y0-(y0-y1)/2]
	p3=[x0,y1]
	p4=[x1,y1]
	l1=[p1,p2]
	l2=[p2,p3]
	l3=[p3,p4]
	return [l1,l2,l3]

def serpinski(depth,lines=[],start=True,x=0,y=0,size=100):
	if start:
		lines=[[[x,y],[x+size,y]]]
	# print(lines)
	newLines=[]
	for line in lines:
		if line[0][1]==line[1][1] and line[0][0]<line[1][0]:
			for nl in rightHorizNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
		if line[0][1]==line[1][1] and line[0][0]>line[1][0]:
			for nl in leftHorizNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
		elif (line[0][0]<line[1][0] and line[0][1]<line[1][1]):
			for nl in upRightNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
		elif (line[0][0]>line[1][0] and line[0][1]>line[1][1]):
			for nl in downLeftNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
		elif (line[0][0]<line[1][0] and line[0][1]>line[1][1]):
			for nl in downRightNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
		elif(line[0][0]>line[1][0] and line[0][1]<line[1][1]):
			for nl in upLeftNL(line[0][0],line[0][1],line[1][0],line[1][1]):
				newLines.append(nl)
	if depth>1:
		return serpinski(depth-1,lines=newLines,start=False)
	else:
		out=[]
		for line in newLines:
			# print(line)
			out.append(line[0])
		out.append(newLines[-1][1])
		print(out)

def add_const(x,y,lis):
	out=[]
	for item in lis:
		out.append([item[0]+x,item[1]+y])
	return out

def mult_const(x,y,lis):
	out=[]
	for item in lis:
		out.append([item[0]*x,item[1]*y])
	return out