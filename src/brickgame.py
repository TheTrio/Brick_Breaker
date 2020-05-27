import pygame
colour=0
colour2=0
colour3=0
from random import randrange
bricky=pygame.image.load('Resources/brick.png')
from time import sleep
class player:
	def __init__(self):
		self.vel=10
		self.height=30
		self.width=100
		self.x=300
		self.y=650
		self.vel=5
		self.hitbox=(self.x,self.y,self.width,self.height)
	def moveleft(self):
		if self.x>0:
			self.x-=self.vel
			self.hitbox=(self.x,self.y,self.width,self.height)
	def moveright(self):
		if self.x<600-self.width:
			self.x+=self.vel
			self.hitbox=(self.x,self.y,self.width,self.height)
class balls:
	def __init__(self, arg=5):
		self.arg = arg
		self.x=paddle.x+paddle.width//2-10
		self.y=paddle.y-40
		self.radius=40
		self.hitbox=(self.x+5,self.y,self.radius,self.radius)
		self.hvel=0
		self.vvel=-arg
	def jump(self):
		if randrange(2)==1:
			self.hvel=self.arg
		else:
			self.hvel=-self.arg
	def bouncevert(self):
		self.vvel*=-1
	def bounshori(self):
		self.hvel*=-1
		
			
class brick:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.width=80
		self.height=50
		self.hitbox=(self.x,self.y,self.width,self.height)
pygame.font.init()
font=pygame.font.SysFont('comicsans',30,True,True)
lives=3
livelist=[pygame.image.load('Resources/pi.png')]
pygame.init()
score=0
boxes=[]
movewith=True
xpos=[0,50,100,150,200,250,300,350,400,450]
combo=10
ypos=[0,50,100,150,200,250,300,350,400,450]
win=pygame.display.set_mode((600,700))



def make_box():
	count = 7
	shift = 0
	for i in range(55,166+55, 55):
		for j in range(0, count):
			boxes.append(brick(shift*85 + j*85, i))
		count-=2
		shift+=1
run=True
paddle=player()
speed = 4
ball=balls(speed)
clock = pygame.time.Clock()
key = pygame.image.load('Resources/ball_t (2).png')
saddle=pygame.image.load("Resources/paddle.png")
background_image = pygame.image.load("Resources/space.jpg")
pygame.mixer.init()
pygame.mixer.music.load('Resources/music.mp3')
pygame.mixer.music.play(-1)
while run:
	win.blit(background_image, [0, 0])
	if lives==0:
		run = False
	else:
		strp=0
		clock.tick(100)
		for i in range(lives):
			win.blit(livelist[0],(strp,0))
			strp+=40
		text = font.render('Score:'+str(score), True,(255,255,0)) 
		win.blit(text,(300,10))
		for event in pygame.event.get():
			if event.type  ==  pygame.QUIT:
				run=False
		if len(boxes)==0:
			speed+=1
			make_box()
			ball = balls(speed)
			if score!=0:
				score+=100
			movewith = True
		for i in boxes:
			win.blit(bricky,i.hitbox)
		win.blit(saddle,paddle.hitbox)
		win.blit(key,(ball.hitbox))
		pygame.display.update()
		keys=pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			paddle.moveleft()
			if movewith==True:
				if ball.x-paddle.vel>0:
					ball.x-=paddle.vel
		elif keys[pygame.K_RIGHT]:
			paddle.moveright()
			if movewith==True:
				if ball.x+paddle.vel<560:
					ball.x+=paddle.vel
		elif keys[pygame.K_SPACE]:
			if movewith:
				ball.jump()
				movewith=False
		
		temp = 0
		if movewith!=True:
			del_index = -1
			for i in range(len(boxes)):
				box = boxes[i]
				if (((box.y + box.height)>=ball.y) and box.y<ball.y) or ((box.y<=ball.y + ball.radius) and (ball.y<box.y+box.height)):
						if ball.hvel<0:
							if (ball.x<=box.x+box.width) and (ball.x+ball.radius>=box.x):
								del_index = i
								ball.bouncevert()
								score+=combo
								combo+=2
						else:
							if (ball.x+ball.radius>=box.x) and (ball.x<=box.x+box.width):
								del_index = i
								ball.bouncevert()
								score+=combo
								combo+=2

			if del_index!=-1:
				del boxes[del_index]

			if ball.y>=700:
				ball = balls(speed)
				lives-=1
				movewith = True
			if ball.x+ball.hvel>0 and ball.x+ball.hvel+ball.radius<560:
				ball.x+=ball.hvel
			else:
				ball.bounshori()
			if ball.y+ball.vvel>0:
				ball.y+=ball.vvel
			else:
				ball.bouncevert()
			if (ball.x>=paddle.x and ball.x<=paddle.x+paddle.width) or (ball.x+40>=paddle.x-5 and ball.x+40<=paddle.x+paddle.width):
				if ball.y+40==paddle.y:
					pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound.wav'))
					temp +=1
					ball.bouncevert()
					combo=10
		ball.hitbox=(ball.x+5,ball.y,ball.radius,ball.radius)