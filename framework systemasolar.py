from visual import *
import random
from visual.graph import * ## invoke graphing routines 
scene.y = 0    # move orbit window below graph 

#scene.width =1024
#scene.height = 1024 
scene.fullscreen = True
#scene.light.
#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mMoon = 7e22
mcraft = 15e3
deltat = 60*60
pscale = 0.1
UA = 1.5182E11 #Unidade astronomica
vOrbitalEarth = ((2* math.pi * UA )/((365 + 1/4 - 1/100 + 1/400)* 24*60**2))
scale = 500
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
	nestedObjects = None
	
	def __init__(self, idPlanet, pos, radius, m, v):
		self.pos = pos
		self.radius = radius
		self.m = m
		self.v = v
		self.idPlanet = idPlanet
		#ids = ids +  1
		self.p = self.v * self.m
		self.lastPos = pos
			
	def upd(self):
		#print("updating obj position")
		#self.inst.pos = self.pos
		#self.inst.radius = self.radius
		if self.nestedObjects is not None:
			for nestO in self.nestedObjects:
				print("updating obj position")
				nestO.pos = self.pos
		#if self.hasArrow is True and self.parr is not None :
		#	self.parr.pos=self.pos
		#	self.parr.axis=self.p
		#if self.hasTrail is True:
		#	self.trail.append(pos=self.pos)
		
		
L = list() #lista de astros


#scaleRadius = 20

scene.lights = []
scene.ambient=color.gray(0.0)
#scene.lights = [distant_light(direction=(-UA, 0, 0), color=color.white(0.8)),distant_light(direction=(-0.88, -0.22, -0.44), color=color.gray(0.3))]



print("velocidade orbital da terra ", vOrbitalEarth)
e = Planet(idPlanet = "Terra", pos = vector(0,0, 0), radius= 6.4E6, m=5.972E24, v=vector(0,vOrbitalEarth, 0) )
e.color = color.blue
e.hasTrail = True
e.material = materials.earth

e.radiusScale = scale * 1#200
e.hasTrail = True
lua = Planet(idPlanet = "lua", pos = vector(4e8, 0, 0), radius=  1.75e6, m=mMoon, v=vector(0,vOrbitalEarth + 1E3, 0) )

lua.color = color.white
lua.hasTrail = True
lua.radiusScale = scale * 1# 200

sun = Planet(idPlanet="sol", pos = vector(-UA , 0, 0), radius=6.95E8, m= 1.989E30, v = vector(0,00000  ,0))
#sun = Planet(idPlanet="sol", pos = vector(-UA , 0, 0), radius=  3000, m=20* 2E30, v = vector(0,0  ,0))
sun.color = color.white
sun.material = materials.emissive
sun.radiusScale = scale * 0.05
#scene.lights = sun.pos

local_light(pos=sun.pos, color=color.white)

L.append(e)
L.append(lua)
L.append(sun)


#debris
#print(random())
avSpeed = 17.9E3
spaceBtweenDebris = 5E7
speedRand = 1E2
for num in range(0, 12):  
	orbitRadius = ((2.8 * UA)) #+ random.randint(-spaceBtweenDebris , spaceBtweenDebris)
	#angle = random.uniform(-2*3.1415, 2*3.1415)
	angle = random.uniform(0,math.pi/15)
	debriSize = random.randint(1E3, 5E5);
	posDebri = vector(math.cos(angle)* orbitRadius - UA,math.sin(angle)*orbitRadius,0)
	modVDebri = avSpeed
	#vDebri = vector(math.cos(angle + 3.1415/2)* modVDebri + random.randint(-speedRand , speedRand) ,math.sin(angle + 3.1415/2)* modVDebri + random.randint(-speedRand , speedRand) ,0)
	vDebri = vector(math.cos(angle + math.pi/2)* modVDebri  + random.randint(-speedRand , speedRand) ,math.sin(angle + math.pi/2)* modVDebri + random.randint(-speedRand , speedRand) ,0)
	print("pos debri = ", str(posDebri))
	print("v debri = ", str(vDebri))
	deb=Planet(idPlanet="debri" + str(num), pos=posDebri, radius= debriSize, m= math.pi * debriSize**2 * 5000 , v=vDebri)
	deb.radiusScale = scale *10#10000
	deb.color =  color.magenta
	L.append(deb)



bn = Planet(idPlanet="Buraco negro", pos=vector(-UA,0,0), radius= 30000, m=10* 2E30, v=vector(0,0,0))
bn.color = color.white
bn.radiusScale = scale *1#100000
bn.material = materials.emissive
#L.append(bn)

venus = Planet(idPlanet = "Venus", pos = vector( -UA + (0.72*UA ),0, 0), radius= 6.2E6, m=0.815 * 5.972E24, v=vector(0,3.5E4, 0) )
venus.color = color.green
venus.radiusScale = scale *1#200
venus.hasTrail = True
L.append(venus)



marte = Planet(idPlanet = "Marte", pos = vector( -UA + (1.52*UA ),0, 0), radius= 3.361E6, m=6.41E23, v=vector(0,24.07E3, 0) )
marte.color = color.red
marte.radiusScale = scale *1#200
marte.hasTrail = True
L.append(marte)




jupiter = Planet(idPlanet = "Jupiter", pos = vector( -UA + (5.454*UA ),0, 0), radius= 69.911E6, m=1.898E27, v=vector(0,13.07E3, 0) )
jupiter.color = color.rgb_to_hsv((0.2,0.1,0.2))
jupiter.radiusScale = scale *1#200
jupiter.hasTrail = True
L.append(jupiter)



saturn = Planet(idPlanet = "Saturn", pos = vector( -UA + (9.554*UA ),0, 0), radius= 58.911E6, m=5.68E26, v=vector(0,13.07E3, 0) )
saturn.color = color.rgb_to_hsv((0.8,0.2,0.6))
saturn.radiusScale = scale *1#200
saturn.hasTrail = True
saturn.nestedObjects = list()
saturn.make_trail=True
#ringSat = ring( pos=saturn.pos, axis=(0,1,1), radius=75.911E9, thickness=0.8 * 35.911E9)

pat = paths.circle( pos=(0,0,600000), radius=85E8 )
tri=shapes.rectangle(pos=(0,100000),  width=45E8, height=45E4)
ess = extrusion(pos=pat, shape=tri, color=color.yellow)

#saturn.nestedObjects.append(ringSat)

	
	
#saturn.initFunc - 
L.append(saturn)

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

while t < 200*365*24*60*60:
	rate(2000)       ## slow down motion to make animation look nicer
	listToRemove = set()
	for astro in L:
		for otherObject in L:
			#calcula forca gravitacional dessse objeto
			if astro.idPlanet != otherObject.idPlanet:
				do = mag(astro.pos - otherObject.pos)
				if do < (astro.radius + otherObject.radius) or astro.pos == otherObject.pos:
					#TODO do colision
					print(astro.idPlanet, "se chocou com ", otherObject.idPlanet)
					if astro.m > otherObject.m:
						listToRemove.add(otherObject)
						astro.m = astro.m + otherObject.m
						astro.radius = astro.radius + otherObject.radius
						astro.inst.radius = otherObject.radiusScale * astro.radius
					else:
						listToRemove.add(astro)
						otherObject.radius = astro.radius + otherObject.radius
						otherObject.m = astro.m + otherObject.m
						otherObject.inst.radius = otherObject.radiusScale * otherObject.radius
				else:
					unitvectorpos = (astro.pos - otherObject.pos)/do
					#force = ((G*astro.m * otherObject.m)/do**2 )* -unitvectorpos
					astro.forces.append(((G*astro.m * otherObject.m)/do**2 )* -unitvectorpos)
					#if t%6E6 == 0:
					#	if astro.idPlanet == "Terra" and otherObject.idPlanet == "sol":
					#		print("Distancia terra sol = ", do, "pos sol=", otherObject.pos)
					#	if astro.idPlanet == "Venus" and otherObject.idPlanet == "sol":
					#		print("Distancia Venus sol = ", do)
		#Atualiza o momento com a forca Pf = Pi+ F.dT
		for f in astro.forces:
			astro.p = astro.p + (f * deltat)

		#atualiza a posicao com a velocidade obtida do momento dS = (p\m).dT
		astro.pos = astro.pos + ((astro.p/astro.m) * deltat)
		astro.inst.pos = astro.pos#astro.inst.pos + astro.p/astro.m * deltat
		astro.upd()

		#apaga as forcas do objeto
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
    
	listToRemove.clear()
	
	t = t+deltat

    

print ('Calculations finished after ',t,'seconds')



