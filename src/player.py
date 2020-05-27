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