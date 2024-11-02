import pgzrun

WIDTH=600
HEIGHT=600

playing=True

black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)

class Circles:
    def __init__(self,size,color,initial_x,initial_y,):
        self.c=color
        self.s=size
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.s,self.c)

GRAVITY=2000.0#pixelspersecond
circle1=Circles(50,green,50,100)

def draw():
    screen.clear()
    circle1.draw()

def update(dt):
    uy=circle1.vy
    circle1.vy+=GRAVITY*dt
    circle1.y+=(uy+circle1.vy)*0.5*dt
    if circle1.y>600:
        circle1.y=600
        circle1.vy=-circle1.vy*0.9

pgzrun.go()