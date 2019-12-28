# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
SCREEN = [WIDTH, HEIGHT] 
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        #self.angle += self.angle_vel
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        if self.thrust:
            canvas.draw_image(self.image, (self.image_center[0]+self.image_center[0]*2, self.image_center[1]), self.image_size, self.pos, self.image_size, self.angle)
        
                                    
    def update(self):
        #print self.vel[0]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
        for val in range(2):
            self.pos[val] = (self.pos[val] + self.vel[val]) % SCREEN[val]
        
        forward = angle_to_vector(self.angle)
        if self.thrust:
            ship_thrust_sound.play()
            forward = angle_to_vector(self.angle)
            const = .02
            #print forward
            self.vel[0] += const * forward[0]
            #print self.vel[0]
            #print self.vel[0]
            self.vel[1] += const * forward[1]
            
        else:
            ship_thrust_sound.rewind()
            #Friction not working Need to be checked
            c = .05
            #print self.vel[0]
            self.vel[0] *= (1-c)
            self.vel[1] *= (1-c)
            
    def shoot(self):
        #global a_missile
        missile_sound.play()
        #self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)
        #print forward
        #print self.vel[0]
        #print a_missile.vel[0]
        #self.pos[0] +=4 * forward[0]
        #self.pos[1] +=4 * forward[1]
        c = 3.5
        #a_missile.pos[0] = self.pos[0] + forward[0] * self.radius
        pos = [0, 0]
        pos[0] = self.pos[0] + forward[0] * self.radius
        #a_missile.pos[1] = self.pos[1] + forward[1] * self.radius
        pos[1] = self.pos[1] + forward[1] * self.radius
        #print forward
        #self.vel[0] += 4 * forward[0]
        #a_missile.vel[0] = self.vel[0] + c * forward[0]
        vel = [0, 0]
        vel[0] = self.vel[0] + c * forward[0]
        #print a_missile.vel[0]
        #self.vel[1] += ( 4 * forward[1])
        #a_missile.vel[1] = self.vel[1] + c * forward[1]
        vel[1] = self.vel[1] + c * forward[1]
        #a_missile.pos[0] += a_missile.vel[0]
        #a_missile.pos[1] += a_missile.vel[1]
        #print pos, vel
        a_missile = Sprite(pos, vel, 0, 0, missile_image, missile_info, sound = missile_sound)
        missile_group.add(a_missile)
        
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        if self.animated:
            canvas.draw_image(self.image, [self.image_center[0]+self.image_center[0]*2*self.age, self.image_center[1]], self.image_size, self.pos, self.image_size)
        
    def update(self):
        self.pos[0] += self.vel[0]
        #print self.pos[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
        for val in range(2):
            self.pos[val] = (self.pos[val] + self.vel[val]) % SCREEN[val]
        self.age+=1
        if self.age>=self.lifespan:
            return False
        elif self.age<=self.lifespan:
            return True
            
    def collide(self, obj):
        return dist(self.get_position(), obj.get_position())< obj.get_radius() + self.get_radius()
    
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
                     
def draw(canvas):
    global time, score, lives, started, rock_group, my_ship
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    #a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    #a_rock.update()
    #print a_missile.pos
    #print a_missile.vel
    #a_missile.update()
    
    if group_collide(rock_group, my_ship):
        lives-=1
    
    if lives==0:
        started = False
        rock_group = set()
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    score+=(group_group_collide(missile_group, rock_group))*10
    
    canvas.draw_text("Lives", (100, 50), 20, 'White')
    canvas.draw_text(str(lives), (100, 75), 20, 'White')
    canvas.draw_text("Score", (650, 50), 20, 'White')
    canvas.draw_text(str(score), (650, 75), 20, 'White')
    
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], splash_info.get_size())
    
# timer handler that spawns a rock    
def rock_spawner():
    #global a_rock
    a = random.randrange(1, 10, 1)/10.0
    b = random.randrange(1, 10, 1)/10.0
    angle_vel = random.randrange(-1, 2, 1)/10.0
    vel = random.randrange(-3, 3, 1)/10.0
    #print a, b
    #a_rock = Sprite()
    #a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [.2, .3], 0, 0.1, asteroid_image, asteroid_info)
    a_rock = Sprite([WIDTH * a , HEIGHT * b], [vel, vel], 0, angle_vel, asteroid_image, asteroid_info)
    if len(rock_group)<12:
        rock_group.add(a_rock)

def process_sprite_group(sprite_group, canvas):
    sprite_Set = set()
    for sprite in sprite_group:
        if not sprite.update():
            sprite_Set.add(sprite)
        sprite.draw(canvas)
    sprite_group.difference_update(sprite_Set)
        
def group_collide(set_of_sprites, other_sprite):
    #global lives
    #sprite_group = set()
    #print len(set_of_sprites)
    for a_sprite in list(set_of_sprites):
        if a_sprite.collide(other_sprite):
            #print "here"
            a_col = Sprite(a_sprite.pos, [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(a_col)
            set_of_sprites.remove(a_sprite)
            return True
    return False
            #sprite_group.add(a_sprite)
            #lives-=1
            #print len(sprite_group)
    #set_of_sprites.difference_update(sprite_group)
    #print len(set_of_sprites)

def group_group_collide(rock_set, missile_set):
    #global score
    collision = 0
    for single_rock in list(rock_set):
        if group_collide(missile_set, single_rock):
            rock_set.discard(single_rock)
            collision+=1
            #score+=20
    return collision
        
        
# define keyhandlers to control firing_angle
def keydown(key):
    global my_ship
    if simplegui.KEY_MAP["space"] == key:
        my_ship.shoot()        
    elif simplegui.KEY_MAP["left"] == key:
        my_ship.angle_vel -= .05
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.angle_vel += .05
    elif simplegui.KEY_MAP["up"] == key:        
        my_ship.thrust = True

def keyup(key):
    global my_ship
    if simplegui.KEY_MAP["left"] == key:
        my_ship.angle_vel += .05
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.angle_vel -= .05
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.thrust = False
        #c = .5
        #print my_ship.vel[0]
        #my_ship.vel[0] *= (1-c)
        #my_ship.vel[1] *= (1-c)
def click(pos):
    global score, lives, started
    if started == False:
        score = 0
        lives = 3
        started = True
        soundtrack.play()
           
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [.2, .3], 0, 0.1, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
missile_group = set()
rock_group = set()
explosion_group = set()
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling

timer.start()
frame.start()