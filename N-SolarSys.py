

class Entity:
	def __init__(self, x, y, vx, vy, X, Y, m):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.m = m
		self.X = X
		self.Y = Y

		
Sun = Entity(0,0,	0,30e3,	[],[],	1.989e30)
Sun2 = Entity(-40e9,0,	0,-30e3,	[],[],	1.989e30)
Sun3 = Entity(0,-1000.641e9,	0,50e3,	[],[],	1.989e30)
Mercury = Entity(57.909e9,0,	0,47.36e3,	[],[],	0.33011e24)
#Mercury2 = Entity(-57.909e9,0,	0,-47.36e3,	[],[],	0.33011e24)
Venus = Entity(108.209e9,0,	0,35.02e3,	[],[],	4.8675e24)
Earth = Entity(149.596e9,0,	0,29.78e3,	[],[],	5.9724e24)
Moon = Entity(1.499804e11,0,	0,28.6e3,	[],[],	7.342e22)

System = [Sun, Sun2, Sun3, Mercury, Venus, Earth, Moon]


t = 0
t_end = 86400*365*10
dt = 86400
G = 6.67e-11
#mercX = []
#mercY = []
#sunX = []
#sunY = []

T = []



while t < t_end:

	for body in System:
		AccelerationX = 0
		AccelerationY = 0
		for bodies in System:
			if bodies != body:
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
	
	
	#mercX.append(Mercury.x)
	#mercY.append(Mercury.y)
	#sunX.append(Sun.x)
	#sunY.append(Sun.y)
	T.append(t)
	t += dt
	

#plt.plot(sunX,sunY)
#plt.show()
import numpy as np
import matplotlib.pyplot as plt
color = ['red', 'green', 'blue', 'orange', 'black']
fig, ax = plt.subplots()
line, = ax.plot(Sun.X[:1], Sun.Y[:1])
#ax.set_xlim(-1000e9,1000e9)
#ax.set_ylim(-1000e9,1000e9)


def buildmebarchart(i=int):
	plt.cla()
	ax.set_xlim(-200e9,1000e9)
	ax.set_ylim(-1000e9,200e9)
	ax.text(100e9,100e9 , 'time = %0.1f' %(i*dt/(86400*365)))
	#ax.set_xlim(57e9,59e9)
	#ax.set_ylim(-1e9,1e9)
	for j in range(len(System)):
		start = max((i-10, 0))
		if j <= 2: 
			line, = ax.plot(System[j].X[:i], System[j].Y[:i], color = 'red', marker = 'o', markersize = 0.5)
		elif j == 3:
			line, = ax.plot(System[j].X[start:i], System[j].Y[start:i], color = 'green', linewidth = 0.8)
		else:
			line, = ax.plot(System[j].X[:i], System[j].Y[:i], color = 'black', linewidth = 1)
		
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
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 1, save_count = 400)
#plt.show()

import matplotlib as mpl 
mpl.rcParams['animation.ffmpeg_path'] = r'C:\\python\\ffmpeg\\bin\\ffmpeg.exe'
writervideo = ani.FFMpegWriter(fps=60) 
animator.save('N-body.mp4', writer=writervideo, dpi = 600)
#writergif = ani.PillowWriter(fps=30)
#animator.save('N-body.gif', writer=writergif, dpi = 600)
plt.close

