# convert frames to gif
import sys,os,subprocess,time

def progress_bar(current,maximum,size=100):
	progress=int(current/maximum*size)

	bar_chars=['[','-',']','[','#',']']
	bar_chars=['','','','','',''] # If you don't use Fira Code font, comment out this line
	
	bar='\r'+bar_chars[0+(3 if progress>0 else 0)]+bar_chars[4]*progress+bar_chars[1]*(size-progress)+bar_chars[2+(3 if progress==size else 0)]+f' {round(current/maximum*100,2)}% done'+'\n'*(size==progress)
	
	sys.stdout.write(bar)
	sys.stdout.flush()

def number_component(x):
	return int(x.split('e')[1].split('.')[0])

def convert(size=1000,delay=10,name='frame'):
	if sys.platform.startswith('linux'):
		start=time.time()
		maximum=len(os.listdir('svg_frames'))-1
		path_lis=sorted(os.listdir('svg_frames'),key=number_component)
		os.system('rm ./png_frames/*')
		print('Converting frames to .png')
		for i,path in enumerate(path_lis):
			if path.startswith(name):
				command=f'--export-background=1 --export-background-opacity=1 --export-width={size} --export-type=png --export-filename=png_frames/{path[:-4]}.png svg_frames/{path}'.split(' ')
				command=['inkscape']+command
				out=subprocess.run(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
				# print(out)
				progress_bar(i,maximum)
				if out.returncode!=0:
					print()
					command=' '.join(out.args)
					raise Exception(f'Error: {command} returned the error code {out.returncode}')
		print('Making gif')
		gifn=len(os.listdir('gifs'))
		os.chdir('./png_frames')
		os.system(f'convert -delay {delay} -loop 1 $(ls -1 | sort -n -t\'e\' -k2) ../gifs/anim{gifn}.gif')
		os.chdir('..')
		end=time.time()
		print(f'Took {end-start} seconds')
# if __name__ == '__main__':
	# convert()
