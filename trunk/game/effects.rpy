label effects:
  transform fadein(delay):
    alpha 0.0
    linear delay alpha 1.0
    
  transform fadeout(delay):
    alpha 1.0
    linear delay alpha 0.0
    
  transform slide(delay, x, y):
    linear delay xpos x ypos y
    
#-----------------------
# GLOW EFFECT
#----------------------
init:
     python:
         def silhouette_matrix (r,g,b,a=1.0):
             return im.matrix((0, 0, 0, 0, r, 
                               0, 0, 0, 0, g,
                               0, 0, 0, 0, b,
                               0, 0, 0, a, 0,))
         def silhouetted (filename, r,g,b, a = 1.0):
             return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))
# this is the logo from the tutorial game (needed for this example)
# image logo = "logo.png"
# and here's a version converted to a white silhouette
# image logo_whiteout = silhouetted ('logo.png',1,1,1)
 
# label start:
    # now we use some ATL to overlay the 'glow' on the logo and cycle its alpha.
#    show logo:
#        xalign 0.5 yalign 0.0
#    show logo_whiteout:
#        xalign 0.5 yalign 0.0 alpha 0.0
#        ease 1.0 alpha 0.95
#        ease 1.0 alpha 0.0
#        repeat
#    "Here we have the amaaazing glowing logo!\n\n{b}TADAAAA!{/b}"

#--------------------------------------------------
# MULTIPLE TRANSITION EFFECTS
#--------------------------------------------------
# Remember that it must be an odd number in total, where in odd numbers are displayables
# and even numbers are the transitions.

init:
    $ teleport = MultipleTransition([False, dissolve, "#fff", dissolve, False, 
                                     dissolve, "#fff", dissolve,
                                     True, dissolve, "#fff", dissolve, True])

#----------------------------------------------
# SCREEN SHAKING LONGTERM
#----------------------------------------------
# This shakes the screen in all directions.   
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#Now it can be used to make quicky shakes!
# The numbers inside Shake(position, duration, maximum distance), time, pixel distance
# High pixel distances are REALLY intense.
#Shake takes the "at" command, not the "with" command.


#-----------------------------------------
# Double Vision/Nausea Effect
#----------------------------------------

init:

    transform transpa:

        alpha 0.5

    python hide:

        def gen_randmotion(count, dist, delay):

            import random

            args = [ ]

            for i in range(0, count):
                args.append(anim.State(i, None,
                                       Position(xpos=random.randrange(-dist, dist),
                                                ypos=random.randrange(-dist, dist),
                                                xanchor='left',
                                                yanchor='top',
                                                )))

            for i in range(0, count):
                for j in range(0, count):

                    if i == j:
                        continue

                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))

            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(15, 15, 3.0)


init python:

    def double_vision_on(picture):

        renpy.show(picture)

        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")

        renpy.with_statement(dissolve)


    def double_vision_off():

        renpy.hide("blur_image")

        renpy.with_statement(dissolve)

        
 #---------------------
 # EXPLOSIONS
 #---------------------
init:
    python:

        class ExplodeFactory: # the factory that makes the particles
           
            def __init__(self, theDisplayable, explodeTime=0, numParticles=100):
                self.displayable = theDisplayable
                self.time = explodeTime
                self.particleMax = numParticles

            def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles()
                return newParticles
                
            
            def createParticles(self):
                timeDelay = renpy.random.random() * 0.6
                return [ExplodeParticle(self.displayable, timeDelay)]
            
            def predict(self):
                return [self.displayable]
    image boom = Particles(ExplodeFactory("gfx/effects/snowflake.png", numParticles=80, explodeTime = 0.5))            
#theDisplayable: The displayable or image name you want to use for your particles
#explodeTime: The time for the burst to keep emitting particles. A value of zero is no time limit.
#numParticles: The limit for the number of particle on screen. 

init:
    python:        
        class ExplodeParticle:
            
            def __init__(self, theDisplayable, timeDelay):
                self.displayable = theDisplayable
                self.delay = timeDelay
                self.xSpeed = (renpy.random.random() - 1.5) * 1.5
                self.ySpeed = (renpy.random.random() - 1.5) * 1.5
                self.xPos = 425
                self.yPos = 325
            
            def update(self, theTime):
                
                if (theTime > self.delay):
                    self.xPos += self.xSpeed * (renpy.random.random() + 5)
                    self.yPos += self.ySpeed * (renpy.random.random() + 5)
                elif (theTime > self.delay):    
                    self.xPos -= self.xSpeed * (renpy.random.random() + 2.5)
                    self.yPos += self.ySpeed * (renpy.random.random() + 2.5)
                elif (theTime < self.delay):    
                    self.xPos -= self.xSpeed * (renpy.random.random() + 5)
                    self.yPos -= self.ySpeed * (renpy.random.random() + 5)
                elif (theTime < self.delay):    
                    self.xPos += self.xSpeed * (renpy.random.random() + 2.5)
                    self.yPos -= self.ySpeed * (renpy.random.random() + 2.5)
                    
                    if self.xPos > 1000 or self.xPos < -1000 or self.yPos > 1000 or self.yPos < -1000 :
                        return None
                
                return (self.xPos, self.yPos, theTime, self.displayable)
## 
# Now you can define the explosion! 
# This uses the show command!


#-----------------------------------------------------
# SNOW EFFECT/RAIN EFFECT!
#----------------------------------------------------

init python:
    
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random numbers we'll generate.
    import random
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=100, speed=250, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        
        #This creates the snow effect. You should use this function instead of instancing
        #the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        #using the default values =D)
        
        #@parm {image} image:
        #    The image used as the snowflakes. This should always be a image file or an im object,
        #    since we'll apply im transformations in it.
        
        #@parm {int} max_particles:
        #    The maximum number of particles at once in the screen.
            
        #@parm {float} speed:
        #    The base vertical speed of the particles. The higher the value, the faster particles will fall.
        #    Values below 1 will be changed to 1
            
        #@parm {float} wind:
        #    The max wind force that'll be applyed to the particles.
            
        #@parm {Tuple ({int} min, {int} max)} xborder:
        #    The horizontal border range. A random value between those two will be applyed when creating particles.
            
        #@parm {Tuple ({int} min, {int} max)} yborder:
        #    The vertical border range. A random value between those two will be applyed when creating particles.
        #    The higher the values, the fartest from the screen they will be created.
        
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        
        #The factory that creates the particles we use in the snow effect.
        
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            
            #Initialize the factory. Parameters are the same as the Snow function.
                        
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles
            
            # the particle's speed
            self.speed = speed
            
            # the wind's speed
            self.wind = wind
            
            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder
            
            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depth = kwargs.get("depth", 10)
            
            # initialize the images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            
            #This is internally called every frame by the Particles object to create new particles.
            #We'll just create new particles if the number of particles on the screen is
            #lower than the max number of particles we can have.
            
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for the particle
                depth = random.randint(1, self.depth)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        
        
        def image_init(self, image):
            
            #This is called internally to initialize the images.
            #will create a list of images with different sizes, so we
            #can predict them all and use the cached versions to make it more memory efficient.            
            
            rv = [ ]
            
            # generate the array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            
            #This is called internally by the Particles object to predict the images the particles
            #are using. It's expected to return a list of images to predict.
             
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        
        #Represents every particle in the screen.
        
        def __init__(self, image, wind, speed, xborder, yborder):
            
            #Initializes the snow particle. This is called automatically when the object is created.
            
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            # the horizontal/vertical positions of this particle            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            
            #Called internally in every frame to update the particle.
            
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # verify if the particle went offscreen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None
                
            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image
            
# And now to call it up in the game!
#This uses a show command!
#Changing the image there will allow us to make it rain, instead!
init:
    image snow = Snow("gfx/effects/snowflake.png")
    
#----------------------------------------------
# NOISE IMG DISSOLVE
#-----------------------------------------------
#Takes with command.
init:
    $ noise_dissolve = ImageDissolve(im.Tile("gfx/effects/noisetile.png"), 1.0, 1)
    
#----------------------------------
# STATIC BACKGROUND
#----------------------------------

image static = anim.SMAnimation("a",
        anim.State("a", "noise1.png"),
        anim.State("b", "noise2.png"),
        anim.State("c", "noise3.png"),
        anim.State("d", "noise4.png"),
        anim.State("e", "noise5.png"),
        
        anim.Edge("a", .2, "b", trans=Dissolve(.2, alpha=True)),
        anim.Edge("b", .2, "a", trans=Dissolve(.2, alpha=True)),
        anim.Edge("a", .2, "c", trans=Dissolve(.2, alpha=True)),
        anim.Edge("c", .2, "a", trans=Dissolve(.2, alpha=True)),
        anim.Edge("a", .2, "d", trans=Dissolve(.2, alpha=True)),
        anim.Edge("d", .2, "a", trans=Dissolve(.2, alpha=True)),
        anim.Edge("a", .2, "e", trans=Dissolve(.2, alpha=True)),
        anim.Edge("e", .2, "a", trans=Dissolve(.2, alpha=True)),

        anim.Edge("b", .2, "c", trans=Dissolve(.2, alpha=True)),
        anim.Edge("c", .2, "b", trans=Dissolve(.2, alpha=True)),
        anim.Edge("b", .2, "d", trans=Dissolve(.2, alpha=True)),
        anim.Edge("d", .2, "b", trans=Dissolve(.2, alpha=True)),
        anim.Edge("b", .2, "e", trans=Dissolve(.2, alpha=True)),
        anim.Edge("e", .2, "b", trans=Dissolve(.2, alpha=True)),
        
        anim.Edge("c", .2, "d", trans=Dissolve(.2, alpha=True)),
        anim.Edge("d", .2, "c", trans=Dissolve(.2, alpha=True)),
        anim.Edge("c", .2, "e", trans=Dissolve(.2, alpha=True)),
        anim.Edge("e", .2, "c", trans=Dissolve(.2, alpha=True)),

        anim.Edge("d", .2, "e", trans=Dissolve(.2, alpha=True)),
        anim.Edge("e", .2, "d", trans=Dissolve(.2, alpha=True)),
        )
#This takes the show command! I will need to create 5 noise images before this can work.
#If it moves too slowly, I can change the first number to something lower to speed it up!
#The key for this command is the word "static". Saying "show static" will show it. Hide static will stop it.

#----------------------------------------------------
# CHAR IMAGE TRANSITIONS
#-------------------------------------------

#This takes an at command.            