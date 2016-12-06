from visual import *
import random
from visual.graph import * ## invoke graphing routines 
scene.y = 0    # move orbit window below graph 

scene.width =1024
scene.height = 1024 
#scene.light.
#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mMoon = 7e22
mcraft = 15e3
deltat =60
pscale = 0.1

ids = 0

class Planet(object):
	idPlanet = ""
	radius = 1
	radiusScale = 20
	pos = vector(0,0,0)
	lastPos = vector(0,0,0)
	v = vector(0,0,0)
	m = 1.0
	inst = None 
	forces = list()
	p = vector(0,0,0)
	color = color.red
	hasTrail = False
	hasArrow = False
	trail = None
	parr = None
	material=None
	def __init__(self, idPlanet, pos, radius, m, v):
		self.pos = pos
		self.radius = radius
		self.m = m
		self.v = v
		self.idPlanet = idPlanet
		#ids = ids +  1
		self.p = self.v * self.m
		self.lastPos = pos
			
	def update():
		self.inst.pos = self.pos
		self.inst.radius = self.radius
		#if self.hasArrow is True and self.parr is not None :
		#	self.parr.pos=self.pos
		#	self.parr.axis=self.p
		#if self.hasTrail is True:
		#	self.trail.append(pos=self.pos)
		
		
L = list() #lista de astros


#scaleRadius = 20

scene.lights = []

vOrbitalEarth = ((2* 3.1415 * 1.5E11 )/(365* 24*60**2))
UA = 1.5E11 #Unidade astronomica

print("velocidade orbital da terra ", vOrbitalEarth)
e = Planet(idPlanet = "Terra", pos = vector(0,0, 0), radius= 6.4E6, m=6E24, v=vector(0,vOrbitalEarth, 0) )
e.color = color.blue
e.hasTrail = True
e.material = materials.earth

e.radiusScale = 100
e.hasTrail = True
lua = Planet(idPlanet = "lua", pos = vector(4e8, 0, 0), radius=  1.75e6, m=mMoon, v=vector(0,vOrbitalEarth + 1E3, 0) )

lua.color = color.white
lua.hasTrail = True
lua.radiusScale = 100

sun = Planet(idPlanet="sol", pos = vector(-UA , 0, 0), radius=1 * 6.95E8, m= 2E30, v = vector(0,00000  ,0))
#sun = Planet(idPlanet="sol", pos = vector(-UA , 0, 0), radius=  3000, m=20* 2E30, v = vector(0,0  ,0))
sun.color = color.yellow
sun.material = materials.emissive
sun.radiusScale = 100
scene.lights = sun.pos

local_light(pos=sun.pos, color=color.yellow)

L.append(e)
L.append(lua)
L.append(sun)


#debris
#print(random())
avSpeed = 17.9E6
spaceBtweenDebris = 9000000
#for num in range(0, 2): 
num = 0
debriSize = random.randint(100, 1E5);
posDebri = vector(((2.7 * UA) - UA) + random.randint(-spaceBtweenDebris , spaceBtweenDebris),random.randint(-spaceBtweenDebris , spaceBtweenDebris),0)
vDebri = vector(0,0,0)#vector(0,avSpeed +random.randint(0 , spaceBtweenDebris),0)
print("pos debri = ", str(posDebri))
print("v debri = ", str(vDebri))
deb=Planet(idPlanet="debri", pos=posDebri, radius= 5000000, m= 2000, v=vector(0,0,0))
deb.radiusScale = 10000
deb.color = color.red
L.append(deb)



bn = Planet(idPlanet="Buraco negro", pos=vector(-1.3* UA,0,0), radius= 3000, m=10* 2E30, v=vector(0,0,0))
bn.color = color.white
bn.radiusScale = 100000

#L.append(bn)

venus = Planet(idPlanet = "Venus", pos = vector( -UA + (0.72*UA ),0, 0), radius= 6.2E6, m=0.815 * 6E24, v=vector(0,3.5E4, 0) )
venus.color = color.green
venus.radiusScale = 100
venus.hasTrail = True
L.append(venus)


for astro in L:
	astro.inst = sphere(pos=astro.pos, radius=astro.radiusScale * astro.radius, color=astro.color)
	if astro.material is not None:
		astro.inst.material = astro.material
	if astro.hasArrow is True:
		astro.parr = arrow(color=color.green)
		astro.parr.pos=astro.pos
		astro.parr.axis=astro.p
		
	if astro.hasTrail is True:
		astro.trail = curve(color=color.white)
		
	print("astro :", astro.radius)
	
	
#OBJECTS AND INITIAL VALUES
#Earth = sphere(pos=vector(0,0,0), radius=6.4e6, material=materials.earth)
#Moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
# Choose an exaggeratedly large radius for the
# space craft so that you can see it!
#craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=3e6,color=color.yellow)
#craft = sphere(pos=vector(-3e6 -1*Earth.radius, 0,0), radius=3e6,color=color.yellow)
#vcraft = vector(-2E3,2*3.2638e3,0)
#pcraft = mcraft*vcraft
#pmoon = vector(0, 0.2 * 1E3 * mMoon, 0)


#parr = arrow(color=color.green)
#parr.pos=craft.pos
#parr.axis=pcraft

#trail = curve(color=craft.color)    ## craft trail: starts with no points
t = 0
scene.autoscale = 0       ## do not allow camera to zoom in or out

#Kgraph = gcurve(color=color.yellow) ## create a gcurve for kinetic energy 
#Ugraph = gcurve(color=color.red) ## create a gcurve for potential energy 
#KplusUgraph = gcurve(color=color.cyan) ## create a gcurve for the sum of K+U 

#CALCULATIONS

while t < 30*365*24*60*60:
	rate(2000)       ## slow down motion to make animation look nicer
	listToRemove = list()
	for astro in L:
		for otherObject in L:
			#calcula forca gravitacional dessse objeto
			if astro.idPlanet != otherObject.idPlanet:
				do = mag(astro.pos - otherObject.pos)
				if do < (astro.radius + otherObject.radius) or astro.pos == otherObject.pos:
					#TODO do colision
					print(astro.idPlanet, "se chocou com ", otherObject.idPlanet)
					if astro.m > otherObject.m:
						listToRemove.append(otherObject)
						astro.m = astro.m + otherObject.m
						astro.radius = astro.radius + otherObject.radius
						astro.inst.radius = otherObject.radiusScale * astro.radius
					else:
						listToRemove.append(astro)
						otherObject.radius = astro.radius + otherObject.radius
						otherObject.m = astro.m + otherObject.m
						otherObject.inst.radius = otherObject.radiusScale * otherObject.radius
				#print(do)
				else:
					unitvectorpos = (astro.pos - otherObject.pos)/do
					#astro.forces.append(((G*astro.m * otherObject.m)/do**2 )* -unitvectorpos)
					force = ((G*astro.m * otherObject.m)/do**2 )* -unitvectorpos
					astro.forces.append(force)
					#if astro.idPlanet == "Terra":
					#	print(" obj:", astro.idPlanet, " otherObject=",otherObject.idPlanet, "oo.m=", otherObject.m, "do=", do, " unit vector=", -unitvectorpos, " stro.m", astro.m, " force=", force)
					#print("Forces astro = ", )
    
		for f in astro.forces:
			astro.p = astro.p + (f * deltat)
			#if astro.idPlanet == "Terra":
			#	print("f =" , f, " p=", astro.p)
			

		#del astro.forces
		
					
		#if astro.idPlanet == "Terra":
		#	print("momento ", astro.idPlanet, " - m=",astro.m, " v=" , astro.p/astro.m, " p=", astro.p)
		astro.pos = astro.pos + ((astro.p/astro.m) * deltat)
		astro.inst.pos = astro.inst.pos + astro.p/astro.m * deltat
		astro.update
		#print("p =" , astro.p)
		del astro.forces[:]
		astro.forces = list()
		
					
	for o in listToRemove:
		print("removendo objeto ", o.idPlanet)
		o.visible = False
		o.radius = 1
		if o in L:
			L.remove(o)
		o.inst.visible = False
		del o.inst
		del o
    
    
	t = t+deltat

    

print ('Calculations finished after ',t,'seconds')



