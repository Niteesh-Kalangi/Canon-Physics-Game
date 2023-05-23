import pygame, sys, pygame_widgets, math
from pygame.locals import QUIT
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

b = 0
g = 9.8
m = 10
w = 0
currentPlayer = 0

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
    self.xPos = self.xPos + self.xVel * (time) * 7
    self.yPos = self.yPos - self.yVel * (time) * 7

  def colliding(self):
    if self.xPos > 1000 or self.xPos < 0 or self.yPos < -200:
      return 1
    if self.yPos > 710:
      return 2
    if self.xPos > castle.get_rect().left and self.xPos < castle.get_rect().left + castle.get_rect().width and self.yPos > castle.get_rect().top and self.yPos < castle.get_rect().top + castle.get_rect().height:
      return 3
    if currentPlayer % 2 == 0:
      if self.xPos > cannon2.xPos and self.yPos > cannon2.yPos and self.xPos < cannon2.xPos + cannonImg.get_rect().width and self.yPos < cannon2.yPos + cannonImg.get_rect().height:
        cannon2.health = cannon2.health - 1
        return 4
    else:
      if self.xPos < cannon1.xPos and self.yPos > cannon1.yPos and self.xPos > cannon1.xPos - cannonImg.get_rect().width and self.yPos < cannon1.yPos + cannonImg.get_rect().height:
        cannon1.health = cannon1.health - 1
        return 4
    return 0

    

  #def hitCannon(cannon):
    

class Cannon:
  def __init__(self, health, xPos, yPos):
    self.health = health
    self.xPos = xPos
    self.yPos = yPos

  #def fire(angle, velocity):
    #ball = CannonBall(xPos, yPos, )
    
  
ball = CannonBall(0,0,10.0,10.0)


""" for i in range(400):

  ball.updateVelocity(0.005)
  ball.updatePosition(0.005)
  #print(ball.xVel)
  #print(ball.xPos)
  #print(ball.yVel)
  print(ball.yPos) """


pygame.init()
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Hello World!')


cannonImg = pygame.image.load('assets/cannon.png')
cannonImg = pygame.transform.scale(cannonImg, (80, int(int(cannonImg.get_rect().height) * (80/int(cannonImg.get_rect().width)))))
cannonballImg = pygame.image.load('assets/cannonball.png')
cannonballImg = pygame.transform.scale(cannonballImg, (20, int(int(cannonballImg.get_rect().height) * (20/int(cannonballImg.get_rect().width)))))


cannon1 = Cannon(100, 100, 700)
cannon2 = Cannon(100, 900, 700)

def drawCannon(health, xPos, yPos):
    if xPos > 500:
      cannon_flipped = pygame.transform.flip(cannonImg, True, False)
      DISPLAYSURF.blit(cannon_flipped, (xPos - cannon_flipped.get_rect().width/2, yPos))
    else:
      DISPLAYSURF.blit(cannonImg, (xPos - cannonImg.get_rect().width/2, yPos))

def drawBall(xPos, yPos):
  DISPLAYSURF.blit(cannonballImg, (xPos, yPos))

def fire(ball):
   fire = True
   while fire:
      
      ball.updateVelocity(0.1)
      ball.updatePosition(0.1)
      pygame.time.wait(30)

      if ball.colliding() > 0:
        fire = False
        currentPlayer = currentPlayer + 1
      else:
        DISPLAYSURF.blit(cannonballImg, (ball.xPos, ball.yPos))
        repaint()
        pygame.display.update()

def repaint():
  color = (135, 206, 235)
  pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 0, 1000, 700))
  color = (0,200,0)
  pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 700, 1000, 300))
  drawCannon(cannon1.health, cannon1.xPos, cannon1.yPos)
  drawCannon(cannon2.health, cannon2.xPos, cannon2.yPos)
  drawBall(currentBall.xPos, currentBall.yPos)
  DISPLAYSURF.blit(castle, (DISPLAYSURF.get_width()/2 - castle.get_rect().width/2, 700 - castle.get_rect().height))




castle = pygame.image.load('assets/castle.png')
castle = pygame.transform.scale(castle, (200, int(int(castle.get_rect().height) * (200/int(castle.get_rect().width)))))


rVelSlider = Slider(DISPLAYSURF, 50, 50, 200, 25, min=20, max = 60, step = 0.5)
rAngSlider = Slider(DISPLAYSURF, 50, 100, 200, 25, min = 20, max = 70, step = 1)
lVelSlider = Slider(DISPLAYSURF, 750, 50, 200, 25, min=20, max = 60, step = 0.5)
lAngSlider = Slider(DISPLAYSURF, 750, 100, 200, 25, min = 20, max = 70, step = 1)
rVelOut = TextBox(DISPLAYSURF, 270, 50, 35, 25, fontSize = 20)
rAngOut = TextBox(DISPLAYSURF, 270, 100, 35, 25, fontSize = 20)
lVelOut = TextBox(DISPLAYSURF, 970, 50, 35, 25, fontSize = 20)
lAngOut = TextBox(DISPLAYSURF, 970, 100, 35, 25, fontSize = 20)
rVelOut.setText(rVelSlider.getValue())
rAngOut.setText(rAngSlider.getValue())
lVelOut.setText(lVelSlider.getValue())
lAngOut.setText(lAngSlider.getValue())

fireButton = Button(DISPLAYSURF, 450, 65, 100, 50, text="FIRE", onClick = lambda: fire(currentBall))

pygame.display.update()
while True:
    if currentPlayer % 2 == 0:
      lVelSlider.hide()
      lAngSlider.hide()
      currentBall = CannonBall(cannon1.xPos + cannonImg.get_rect().width/2, cannon1.yPos, math.cos(math.radians(rAngSlider.getValue())) * rVelSlider.getValue(), math.sin(math.radians(rAngSlider.getValue())) * rVelSlider.getValue())
    else:
      rVelSlider.hide()
      rAngSlider.hide()
      currentBall = CannonBall(cannon2.xPos + cannonImg.get_rect().width/2, cannon2.yPos, -1 * math.cos(math.radians(lAngSlider.getValue())) * lVelSlider.getValue(), math.sin(math.radians(lAngSlider.getValue())) * lVelSlider.getValue())
 
    repaint()
    events = pygame.event.get()
    pygame_widgets.update(events)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    rVelOut.setText(rVelSlider.getValue())
    rAngOut.setText(rAngSlider.getValue())
    lVelOut.setText(lVelSlider.getValue())
    lAngOut.setText(lAngSlider.getValue())
    #pygame.time.wait(5)
    #ball.updateVelocity(0.05)
    #ball.updatePosition(0.05)
    pygame_widgets.update(events)
    pygame.display.update()

