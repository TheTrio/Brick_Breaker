class brick:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.width=80
		self.height=50
		self.hitbox=(self.x,self.y,self.width,self.height)