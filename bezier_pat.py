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