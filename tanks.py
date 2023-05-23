import pygame, sys
from pygame.locals import QUIT

b = 0
g = 9.8
m = 10
w = 0

#cannonball class
class CannonBall:
  xPos = 0
  yPos = 0
  xVel = 0
  yVel = 0
  iniXVel = 0
  iniYVel = 0
  lastUpdate = 0
  
  def __init__(self, xPos, yPos, xVel, yVel):
    self.xPos = xPos
    self.yPos = yPos
    self.xVel = xVel
    self.yVel = yVel
    #self.iniXVel = iniXVel
    #self.iniYVel = iniYVel

  def updateVelocity(self, time):
    self.yVel = self.yVel + ((-m*g - b*(self.yVel**2))/m)*(time)
    self.xVel = self.xVel + ((w - b*(self.xVel**2))/m)*(time)
    self.lastUpdate = time

  def updatePosition(self, time):
    self.xPos = self.xPos + self.xVel * (time) * 20
    self.yPos = self.yPos - self.yVel * (time) * 20

  #def hitCannon(cannon):
    

class Cannon:
  def __init__(self, health, xPos, yPos):
    self.health = health
    self.xPos = xPos
    self.yPos = yPos

  #def fire(angle, velocity):
    #ball = CannonBall(xPos, yPos, )
    
  
ball = CannonBall(0,0,10.0,10.0)


for i in range(400):

  ball.updateVelocity(0.005)
  ball.updatePosition(0.005)
  #print(ball.xVel)
  #print(ball.xPos)
  #print(ball.yVel)
  print(ball.yPos)


pygame.init()
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Hello World!')
# Initializing Color
color = (135, 206, 235)
 
# Drawing Rectangle
pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 0, 1000, 700))
color = (0,200,0)
pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 700, 1000, 300))

cannonImg = pygame.image.load('assets/cannon.png')
cannonImg = pygame.transform.scale(cannonImg, (80, int(int(cannonImg.get_rect().height) * (80/int(cannonImg.get_rect().width)))))
cannonballImg = pygame.image.load('assets/cannonball.png')
cannonballImg = pygame.transform.scale(cannonballImg, (20, int(int(cannonballImg.get_rect().height) * (20/int(cannonballImg.get_rect().width)))))


cannon1 = Cannon(100, 100, 700)
cannon2 = Cannon(100, 900, 700)

def drawCannon(health, xPos, yPos):
    if xPos > 500:
      print("over")
      cannon_flipped = pygame.transform.flip(cannonImg, True, False)
      DISPLAYSURF.blit(cannon_flipped, (xPos - cannon_flipped.get_rect().width/2, yPos))
    else:
      print("under")
      DISPLAYSURF.blit(cannonImg, (xPos - cannonImg.get_rect().width/2, yPos))

def drawBall(xPos, yPos):
  DISPLAYSURF.blit(cannonballImg, (xPos, yPos))


drawCannon(cannon1.health, cannon1.xPos, cannon1.yPos)
drawCannon(cannon2.health, cannon2.xPos, cannon2.yPos)
drawBall(cannon1.xPos + cannonImg.get_rect().width/2, cannon1.yPos)

castle = pygame.image.load('assets/castle.png')
castle = pygame.transform.scale(castle, (200, int(int(castle.get_rect().height) * (200/int(castle.get_rect().width)))))

ballOne = CannonBall(cannon1.xPos + cannonImg.get_rect().width/2, cannon1.yPos, 8, 22)
DISPLAYSURF.blit(castle, (DISPLAYSURF.get_width()/2 - castle.get_rect().width/2, 700 - castle.get_rect().height))

fire = True

pygame.display.update()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    while fire:
      
      ballOne.updateVelocity(0.1)
      ballOne.updatePosition(0.1)
      pygame.time.wait(30)

      if ballOne.xPos > DISPLAYSURF.get_width() or ballOne.xPos < 0 or ballOne.yPos > DISPLAYSURF.get_height() or ballOne.yPos < 0:
        fire = False
      else:
        
        DISPLAYSURF.blit(cannonballImg, (ballOne.xPos, ballOne.yPos))

      pygame.display.update()
    
    #pygame.time.wait(5)
    #ball.updateVelocity(0.05)
    #ball.updatePosition(0.05)
    pygame.display.update()

