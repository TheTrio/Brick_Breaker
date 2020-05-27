from player import *
from random import randrange
class balls:
	def __init__(self, paddle, arg=5):
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