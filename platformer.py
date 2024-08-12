import numpy as np
import random
import os,time
from pydub import AudioSegment
from pydub.playback import play
global levelend
levelend=False
'''
song =AudioSegment.from_wav("note.wav")
play(song)
'''
def playerpos(height,width):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				return i,j
def dropleft(height,width):
	global lgpx,lgpy
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]==" "
	#platform[lgpx][lgpy]="@"
	platform[lgpx+4][lgpy-4]="@"
	lgpx+=4
	lgpy-=4
	alive=True
	#for i in range(1,5):
		#platform[]
def dropright(height,width):
	global lgpx,lgpy
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]==" "
	#platform[lgpx][lgpy]="@"
	platform[lgpx+4][lgpy+4]="@"
	lgpx+=4
	lgpy+=4
	alive=True
	#for i in range(1,5):
		#platform[]
def moveright(height,width,px,py):
	global platform
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]=" "
	#platform[px][py]=" "
	platform[px][py+1]="@"
	display(height+3,width+3)
	return platform
def moveleft(height,width,px,py):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]=" "
	platform[px][py]=" "
	platform[px][py-1]="@"
	display(height+3,width+3)
	return platform
def jumpleft(height,width,px,py):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]=" "
	#platform[px][py]=" "
	platform[px][py-4]="@"
	display(height+3,width+3)
	return platform
def jumpright(height,width,px,py):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				platform[i][j]=" "
	#platform[px][py]=" "
	platform[px][py+4]="@"
	display(height+3,width+3)
	return platform
def lendchck(height,width):
	global levelend,platform,alive
	print("got called")
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				if(platform[i][j-1]=="+" or platform[i][j+1]=="+" or platform[i+1][j]=="+" or platform[i-1][j]=="+"):
					print("here",platform[i][j],platform[i][j+1],platform[i][j-1])
					levelend=True
					display(height+3,width+3)
					exit()
				else:
					pass
def alivecheck(height,width):
	global alive,lgpx,lgpy
	if(alive):
		pass
	else:
		return False
def atground(height,width,px,py):
	global lgpx,lgpy
	lgpx=px
	lgpy=py
def walker(platform,height,width,px,py):
	global movelist,levelend,alive,lgpx,lgpy
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				px=i
				py=j
				grounded=False
				while(grounded==False):
					if(platform[px+1][py]=="+" and platform[px][py]=="@"):
						levelend=True
						exit()
					elif(platform[px+1][py]!="-" and platform[px][py]=="@" and platform[px+1][py]!="*" and platform[px+1][py]!="!"):
						platform[px+1][py]="@"
						platform[px][py]=" "
						#platform,grounded=playergravity(height,width,thecharecter)
					elif(platform[px+1][py]=="*"):
						if(movelist[-1]=="6"):
							platform[px][py]=" "
							platform[lgpx][lgpy]="@"
							alive=False
						if(movelist[-1]=="4"):
							platform[px][py]=" "
							platform[lgpx][lgpy]="@"
							alive=False
					else:
						atground(height,width,px,py)
						grounded=True
	lendchck(height,width)
	alivecheck(height,width)
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="@"):
				px=i
				py=j
				break
	flag=False
	print("here0","player location:",px,py)
	if(levelend==False):
		print("here1")
		if(len(movelist)==0 or (len(movelist)==1 and movelist[-1]=="fall")):
			if(random.randint(0,20)%2==0):
				print("4")
				movelist.append("4")
				if(platform[px][py-1]!=" "):
					movelist.pop()
					movelist.append("6") 
					if(platform[px][py+1]=="*"):
						movelist.pop()
						movelist.append("86")
						platform=jumpright(height,width,px,py)
						#platform[px][py+4]="@"
						#platform[px][py]=" "
						#platform,flag=playergravity(height,width,"@")
						lendchck(height,width)
						#display(height+3,width+3)
						walker(platform,height,width,px,py+4)
					else:
						platform=moveright(height,width,px,py)
						#platform[px][py+1]="@"
						#platform[px][py]=" "
						#platform,flag=playergravity(height,width,"@")
						lendchck(height,width)
						#display(height+3,width+3)
						walker(platform,height,width,px,py+1)
				else:
					print("5")
					platform=moveleft(height,width,px,py)
					#platform[px][py-1]="@"
					#platform[px][py]=" "
					#platform,flag=playergravity(height,width,"@")
					lendchck(height,width)
					#display(height+3,width+3)
					walker(platform,height,width,px,py-1)
			else:
				print("here3")
				movelist.append("6")
				if(platform[px][py+1]=="*"):
					movelist.pop()
					movelist.append("86")
					platform=jumpright(height,width,px,py)
					#platform[px][py+4]="@"
					#platform[px][py]=" "
					#platform,flag=playergravity(height,width,"@")
					lendchck(height,width)
					#display(height+3,width+3)
					walker(platform,height,width,px,py+4)
				else:
					print("6")
					platform=moveright(height,width,px,py)
					#platform[px][py+1]="@"
					#platform[px][py]=" "
					#platform,flag=playergravity(height,width,"@")
					lendchck(height,width)
					#display(height+3,width+3)
					walker(platform,height,width,px,py+1)
		else:
			print("here2")
			print("MOVELIST LENGTH:",len(movelist),movelist[-1])
			#if(alive==False and deathby=="fallonspike"):
			if(alive==False):
				if(movelist[-1]=="6"):
					dropright(height,width)
					alive=True
				if(movelist[-1]=="4"):
					dropleft(height,width)
					alive=True
			if(platform[px][py+1]==" " and (movelist[-1]=="6" or movelist[-1]=="86")):
				print("7")
				movelist.append("6")
				platform=moveright(height,width,px,py)
				#platform[px][py+1]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py+1)
			if(platform[px][py-1]==" " and (movelist[-1]=="4" or movelist[-1]=="84" or movelist[-2]=="4")):
				print("8")
				movelist.append("4")
				platform=moveleft(height,width,px,py)
				#platform[px][py-1]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py-1)
			if(platform[px][py+1]=="*" and (movelist[-1]=="6" or movelist[-1]=="86")):
				print("9")
				movelist.append("86")
				platform=jumpright(height,width,px,py)
				#platform[px][py+4]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py+4)
			if(platform[px][py-1]=="*" and (movelist[-1]=="4" or movelist[-1]=="84")):
				print("10")
				movelist.append("84")
				platform=jumpleft(height,width,px,py)
				#platform[px][py-4]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py-4)
			if(platform[px][py+1]=="|"):
				print("11")
				movelist.append("4")
				platform=moveleft(height,width,px,py)
				#platform[px][py-1]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py-1)
			if(platform[px][py-1]=="|"):
				print("12")
				movelist.append("6")
				platform=moveright(height,width,px,py)
				#platform[px][py+1]="@"
				#platform[px][py]=" "
				#platform,flag=playergravity(height,width,"@")
				lendchck(height,width)
				#display(height+3,width+3)
				walker(platform,height,width,px,py+1)
	else:
		return True
def cleanspikes(height,width):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="*"):
				try:
					if(platform[i][3+j]=="*"):
						platform[i][3+j]=" "
				except:
					pass
def spkiespawner(height,width):
	for i in range(1,height):
		nospplatfrom=random.randint(1,6)
		while(nospplatfrom!=0):
			if(platform[i][width]=="-"):
				if(i==4):
					spikepos=random.randint(5,width-5)
				else:
					spikepos=random.randint(0,width-5)
				nos=random.randint(1,3)
				for j in range(nos):
					#if(platform[i+1][j]!=" "):
					platform[i-1][spikepos+j]="*"
						#print("i:",i,"j:",j,"content in i,j:",platform[i][j],"spikepos:",spikepos)
				nospplatfrom-=1
			else:
				nospplatfrom-=1
def spikegravity(height,width,thecharecter):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]==thecharecter):
				px=i
				py=j
				#grounded=False
				#while(grounded==False):
				if(platform[px+1][py]=="+"):
					platform[px][py]=" "
				if(platform[px+1][py]!="-" and platform[px][py]==thecharecter):
					platform[px+1][py]=thecharecter
					platform[px][py]=" "
						#os.system('cls')
						#display(height+3,width+3)
						#grounded=gravity(height,width,px+1,py)
						#grounded=spikegravity(height,width,thecharecter)
	'''
	print("charecter:",thecharecter)
	#print("modx:",px,"mody:",py)
	for i in range(height):
		for j in range(width):
			if(platform[i][j]==thecharecter):
				px=i
				py=j
				if(platform[px+1][py]==" " and (platform[px][py-1]!="-" or platform[px][py+1]!="-")):
					platform[px][py]="-"
	'''
def playergravity(height,width,thecharecter):
	global platform,alive
	#print("charecter:",thecharecter)
	#print("modx:",px,"mody:",py)
	for i in range(height):
		for j in range(width):
			if(platform[i][j]==thecharecter):
				px=i
				py=j
				grounded=False
				while(grounded==False):
					if(platform[px+1][py]=="+" and platform[px][py]=="@"):
						levelend=True
					elif(platform[px+1][py]!="-" and platform[px][py]==thecharecter and platform[px+1][py]!="*"):
						platform[px+1][py]=thecharecter
						platform[px][py]=" "
						platform,grounded=playergravity(height,width,thecharecter)
					elif(platform[px+1][py]=="*"):
						alive=False

					else:
						grounded=True
						'''
						os.system('cls')
						print("GRAVITY")
						for i in range(height+2):
							for j in range(width+2):
								print(platform[i][j],end=' ')
							print(" ")
						time.sleep(1)
						'''
						return platform,grounded
	'''
	grounded=False
	while(grounded==False):
		if(platfomr[px+1][py]=="+" and platform[px][py]=="@"):
			levelend=True
		if(platform[px+1][py]!="-" and platform[px][py]==thecharecter):
			platform[px+1][py]=thecharecter
			platform[px][py]=" "
			#os.system('cls')
			if(len(movelist)==0):
				movelist.append("fall")
			if(movelist[-1]!="fall"):
				movelist.append("fall")
			display(height+3,width+3)
			#grounded=gravity(height,width,px+1,py)
			grounded=playergravity(height,width,thecharecter)
		else:
			return True
	'''
def playerspawner(height,width):
	x=1
	y=1
	platform[x][y]="@"
	return x,y
def opener(modhieght,width,flag,lastopen):
	start=1
	spot=False
	end=int(width)
	if(flag!=0):
		while(spot==False):
			openpoint=random.randint(0,1000)
			if((openpoint%3)==2 and lastopen==0):
				pass
			elif((openpoint%3)==1 and lastopen==1):
				pass
			elif((openpoint%3)==0 and lastopen==2):
				pass
			else:
				spot=True
		if((openpoint%3)==0):
			for i in range(3):
				platform[modhieght][end-i]=" "
			lastopen=2
			return lastopen
		elif((openpoint%3)==1):
			middle=int(width/2)-1
			for i in range(3):
				platform[modhieght][middle+i]=" "
			lastopen=1
			return lastopen
		else:
			for i in range(3):
				platform[modhieght][start+i]=" "
			lastopen=0
			return lastopen
	else:
		portalpos=random.randint(0,100)
		modhieght-=1
		if((portalpos%2)==0):
			platform[modhieght][end]="+"
			platform[modhieght][end-1]="+"
			platform[modhieght-1][end]="+"
			platform[modhieght-1][end-1]="+"
		else:
			platform[modhieght][start]="+"
			platform[modhieght-1][start]="+"
			platform[modhieght-1][start+1]="+"
			platform[modhieght][start+1]="+"
def platformmaker(height,width,compartments):
	flag=compartments
	modhieght=0
	modhieght+=4
	lastopen=0
	while(flag!=0 and modhieght<=height):
		for i in range(1,width+1):
			platform[modhieght][i]="-"
		flag-=1
		lastopen=opener(modhieght,width,flag,lastopen)
		modhieght+=4
def border(height,width):
	for i in range(width):
		platform[0][i]="|"
	for i in range(height):
		platform[i][0]="|"
	for i in range(width):
		platform[height-2][i]="|"
	for i in range(height):
		platform[i][width-2]="|"
def heightrandomiser():
	theight=random.randint(2,15)
	theight=theight*4
	return theight
def spikelocker(height,width):
	for i in range(height):
		for j in range(width):
			if(platform[i][j]=="*"):
				spikeloc[i][j]="1"
height=heightrandomiser()
#height=8
width=50#100
print(height,width)
#platform=np.zeros([height, width],dtype=int)#[height][width]
platform=[[" " for _ in range(width+3)] for _ in range(height+3)]
spikeloc=[["0" for _ in range(width+3)] for _ in range(height+3)]
def display(height,width):
	os.system('cls')
	for i in range(height-1):
		for j in range(width-1):
			print(platform[i][j],end=' ')
		print(" ")
	try:
		print(movelist[-1])
		#time.sleep(1)
	except:
		pass
		#time.sleep(1)
	time.sleep(0.5)
compartments=height/4
border(height+3,width+3)
simple=False
player="@"
spike="*"
lgpx=0
lgpy=0
alive=True
inground=False
movelist=[]
platformmaker(height,width,compartments)
playerx,playery=playerspawner(height,width)
#gravity(height,width,playerx,playery,player)
platform,inground=playergravity(height,width,player)
playerx,playery=playerpos(height,width)
spkiespawner(height,width)
spikelocker(height,width)
#os.system('cls')
display(height+3,width+3)
spikegravity(height,width,spike)
#playergravity(height,width,spike)
cleanspikes(height,width)
#os.system('cls')
border(height+3,width+3)
#walker(platform,height,width,playerx,playery)
display(height+3,width+3)
print("player X:",playerx)
print("player Y:",playery)
#os.system('cls')
availmoves=["4","6","86","84"]
walker(platform,height,width,playerx,playery)
display(height+3,width+3)
print("MOVES DONE:",movelist)