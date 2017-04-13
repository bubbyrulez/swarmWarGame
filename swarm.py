class swarm:
	def __init__(self,mode,posx,posy,vx,vy):
		self.mode = mode
		self.pos[0] = posx
		self.pos[1] = posy
		self.velocity[0] = vx
		self.velocity[1] = vy

	def move(self,v):
		if(self.mode == ''):
			if(self.position !> worldBorder or self.position !< -worldBorder):
				self.pos = self.pos + self.velocity


