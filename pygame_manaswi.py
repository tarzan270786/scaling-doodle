import pygame
import random
clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")
class obstacle(object):
    def __init__(self,x,y,width,height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
def generate_random():
    var = random.randint(1,4)
run = True
x=int(input("Enter x\n"))
y=int(input("Enter y\n"))
vel=int(input("Enter vel\n"))
dot= obstacle(x,y,10,10,vel)
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    generate_random()
    if keys[pygame.K_LEFT] and dot.x> dot.vel: 
    if var == 1:
        dot.x -= dot.vel
        generate_random()
    #if keys[pygame.K_RIGHT] and dot.x< 500- dot.width- dot.vel:
    if var == 2:
        dot.x+= dot.vel
        generate_random()
    #if keys[pygame.K_UP] and dot.y>dot.vel:
    if var == 3:
        dot.y-= dot.vel
        generate_random()
    #if keys[pygame.K_DOWN]  and dot.y< 500- dot.width- dot.vel:
    if var == 4:
        dot.y+= dot.vel
        generate_random()
    win.fill((0,0,0))
    pygame.draw.rect(win,(250,0,0), (dot.x,dot.y,dot.width,dot.height))
    pygame.display.update()


pygame.quit()
