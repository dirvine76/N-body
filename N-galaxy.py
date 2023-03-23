import numpy as np
import random

class Entity:
	def __init__(self, x, y, vx, vy, X, Y, m):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.m = m
		self.X = X
		self.Y = Y

#Setup for various bodies and parameters		
Sun = Entity(-100e9,0,	10e3,-20.2e3,	[],[],	1.989e30)
Sun2 = Entity(50e9,0,	0,30.2e3,	[],[],	1.989e30)
Sun3 = Entity(0,-1000.641e9,	0,50e3,	[],[],	1.989e30)
Mercury = Entity(57.909e9,0,	0,47.36e3,	[],[],	0.33011e24)
#Mercury2 = Entity(-57.909e9,0,	0,-47.36e3,	[],[],	0.33011e24)
Venus = Entity(108.209e9,0,	0,35.02e3,	[],[],	4.8675e24)
Earth = Entity(149.596e9,0,	0,29.78e3,	[],[],	5.9724e24)
Moon = Entity(1.499804e11,0,	0,28.6e3,	[],[],	7.342e22)
t = 0
t_end = 86400*365*4
dt = 86400
G = 6.67e-11

#creates a uniformly distributed N bodies of mass 1e12 kg in a radius R
def genGal(x,y,vx,vy,M,N,R):
	galaxy = []
	for i in range(N):
		dist = random.uniform(R/12,R)
		theta = random.uniform(0,2*np.pi)
		dx = dist*np.cos(theta)
		dy = dist*np.sin(theta)
		dvx = ((G*M/dist)**(1/2))*np.sin(theta)
		dvy = ((G*M/dist)**(1/2))*np.cos(theta)
		galaxy.append(Entity(x+dx,y+dy,	vx-dvx, vy+dvy, [],[], 1e12))
	return galaxy
	
#Creates a System list which contains all entities
System = [Sun, Sun2]
System = System + genGal(Sun.x,Sun.y,Sun.vx,Sun.vy,1.989e30,300, 100e9) + genGal(Sun2.x,Sun2.y,Sun2.vx,Sun2.vy,1.989e30,300, 100e9)







T = []


#Physics engine
#while t < t_end:

#	for body in System:
#		AccelerationX = 0
#		AccelerationY = 0
#		for bodies in System:
#			if bodies != body:
#				rx = bodies.x - body.x
#				ry = bodies.y - body.y
#				dist = (rx**2 + ry**2)**(1/2)
				
#				ax = 1*bodies.m*G*rx/(dist**3)
#				ay = 1*bodies.m*G*ry/(dist**3)
				
#				AccelerationX += ax
#				AccelerationY += ay
			
#		body.vx += AccelerationX*dt
#		body.vy += AccelerationY*dt
	
#	for body in System:
#		body.x += body.vx * dt
#		body.y += body.vy * dt
#		body.X.append(body.x)
#		body.Y.append(body.y)
	
	
	
#	T.append(t)
#	t += dt
	
while t < t_end:

	for body in System:
		AccelerationX = 0
		AccelerationY = 0
		for bodies in System:
			if bodies != body and bodies.m > 1e28:
				rx = bodies.x - body.x
				ry = bodies.y - body.y
				dist = (rx**2 + ry**2)**(1/2)
				
				ax = 1*bodies.m*G*rx/(dist**3)
				ay = 1*bodies.m*G*ry/(dist**3)
				
				AccelerationX += ax
				AccelerationY += ay
			
		body.vx += AccelerationX*dt
		body.vy += AccelerationY*dt
	
	for body in System:
		body.x += body.vx * dt
		body.y += body.vy * dt
		body.X.append(body.x)
		body.Y.append(body.y)
	
	
	
	T.append(t)
	t += dt


#Plot setup
import matplotlib.pyplot as plt
color = ['red', 'green', 'blue', 'orange', 'black']
fig, ax = plt.subplots()
line, = ax.plot(Sun.X[:1], Sun.Y[:1])
#ax.set_xlim(-1000e9,1000e9)
#ax.set_ylim(-1000e9,1000e9)

#Animate function
def buildmebarchart(i=int):
	plt.cla()
	ax.set_xlim(-200e9,200e9)
	ax.set_ylim(-200e9,200e9)
	ax.text(100e9,100e9 , 'time = %0.1f' %(i*dt/(86400*365)))
	#ax.set_xlim(57e9,59e9)
	#ax.set_ylim(-1e9,1e9)
	for j in range(len(System)):
		start = max((i-3, 0))
		if j <= 1: 
			line, = ax.plot(System[j].X[:i], System[j].Y[:i], color = 'red', marker = 'o', markersize = 0.5)
		else:
			line, = ax.plot(System[j].X[start:i], System[j].Y[start:i], color = 'black', linewidth = 1)
		
		#if j == 3:
		#	line, = ax.plot(System[j].X[start:i], System[j].Y[start:i], color = 'green', linewidth = 0.8)
		#elif j==4:
		#	line, = ax.plot(System[j].X[start:i], System[j].Y[start:i], color = 'black', linewidth = 0.8)
		
		#line.set_data(System[j].X[start:i], System[j].Y[start:i])
		#line.set_color(color[j])
		#if i < 10:
			#plt.plot(System[j].X[:i], System[j].Y[:i], color = color[j])
		#else:
			#plt.plot(System[j].X[(i-10):i], System[j].Y[(i-10):i], color = color[j])
		#p[j].set_color('red')
	#note it only returns the dataset, up to the point i
    #for i in range(0,4):
    #    p[i].set_color(color[i]) #set the colour of each curve


import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 1, save_count = 500)
#plt.show()




import matplotlib as mpl 
mpl.rcParams['animation.ffmpeg_path'] = r'C:\\python\\ffmpeg\\bin\\ffmpeg.exe'
writervideo = ani.FFMpegWriter(fps=60) 
animator.save('N-deflection.mp4', writer=writervideo, dpi = 600)
plt.close

