from visual import *
from visual.graph import * ## invoke graphing routines 
scene.y = 400    # move orbit window below graph 

scene.width =1024
scene.height = 760

#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mMoon = 7e22
mcraft = 15e3
deltat = 60
pscale = 0.1

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, material=materials.earth)
Moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
# Choose an exaggeratedly large radius for the
# space craft so that you can see it!
#craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=3e6,color=color.yellow)
craft = sphere(pos=vector(-3e6 -1*Earth.radius, 0,0), radius=3e6,color=color.yellow)
vcraft = vector(-2E3,3.2638e3,0)
pcraft = mcraft*vcraft
pmoon = vector(0, 0.2 * 1E3 * mMoon, 0)


parr = arrow(color=color.green)
parr.pos=craft.pos
parr.axis=pcraft

trail = curve(color=craft.color)    ## craft trail: starts with no points
t = 0
scene.autoscale = 0       ## do not allow camera to zoom in or out

Kgraph = gcurve(color=color.yellow) ## create a gcurve for kinetic energy 
Ugraph = gcurve(color=color.red) ## create a gcurve for potential energy 
KplusUgraph = gcurve(color=color.cyan) ## create a gcurve for the sum of K+U 

#CALCULATIONS

while t < 10*365*24*60*60:
    rate(2000)       ## slow down motion to make animation look nicer
    ## you must add statements for the iterative update of 
    ## gravitational force, momentum, and position
    r = craft.pos-Earth.pos
    rmoon = craft.pos-Moon.pos
    rmag = mag(r)
    rmoonmag = mag(rmoon)
    rhat = r/rmag
    Fearth = -(G*mEarth*mcraft/rmag**2)*rhat

    rm = craft.pos-Moon.pos
    rmmag = mag(rm)
    rmhat = rm/rmmag
    Fmoon = -(G*mMoon*mcraft/rmmag**2)*rmhat
    
    
    #orbita da lua
    dEM = sqrt((Moon.pos.x - Earth.pos.x)**2 + (Moon.pos.y - Earth.pos.y)**2)
    
    unitVectorDEarthMoon = vector((Moon.pos.x - Earth.pos.x)/dEM, (Moon.pos.y - Earth.pos.y)/dEM, 0)
    
    fEM = (G*mMoon*mEarth/(mag(Moon.pos - Earth.pos))**2)* (-unitVectorDEarthMoon)
    
    pmoon = pmoon + fEM * deltat
    
    Moon.pos = Moon.pos + pmoon/mMoon * deltat
    
    #fim orbita lua
    
    Fnet = Fearth + Fmoon
    
    pcraft = pcraft+Fnet*deltat
    craft.pos = craft.pos+pcraft/mcraft*deltat

    parr.pos=craft.pos
    parr.axis=pcraft


	#if rmoonmag < Earth.radius:
	#	break
	

    if rmag < Earth.radius:	
		break


    ## check to see if the spacecraft has crashed on the Earth.
    ## if so, get out of the calculation loop

    K = mag(pcraft)*mag(pcraft)/(2*mcraft) ## you must complete this line
    U = -G*mMoon*mcraft/rmmag - G*mEarth*mcraft/rmag## you must complete this; omit the constant term for the Earth-Moon interaction 
    Kgraph.plot(pos=(t,K))   ## add a point to the kinetic energy graph 
    Ugraph.plot(pos=(t,U))   ## add a point to the potential energy graph 
    KplusUgraph.plot(pos=(t,K+U))  ## add a point to the K+U graph 

    trail.append(pos=craft.pos)
     ## this adds the new position of the spacecraft to the trail
    t = t+deltat
    

print ('Calculations finished after ',t,'seconds')
