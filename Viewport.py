from Vector2D import *
from Vector3D import *
import globals

class Viewport:
	def __init__(self):
		self.center = Vector3D(-10,10)
		self.land_sprites  = []
		self.world_sprites = []
				
	def clear(self):
		globals.canvas.delete("all")
		
		
	def draw(self):
		del self.land_sprites[:]
		
		for sprite in globals.land.sprites:
			loc = sprite.getLocation()
			pos = self.project(loc)
			if pos.x > 0 and pos.x < 800 and pos.y > 0 and pos.y < 600:
				self.land_sprites.append(sprite)
		
		for sprite in self.land_sprites:
			sprite.draw()
		
		for sprite in globals.world.sprites:
			loc = sprite.getLocation()
			pos = self.project(loc)
			if pos.x > 0 and pos.x < 800 and pos.y > 0 and pos.y < 600:
				self.world_sprites.append(sprite)
		
		
		for sprite in self.world_sprites:
			sprite.draw()
		
		pass
		
	def getCenter(self):
		return Vector3D(self.center.x, self.center.y, 0)
	
	def setCenter(self, center):
		self.center = center
		
	def project(self, location):
		''' Project from world location to world position '''
		x = (location.x - location.y) * 32
		y = (location.x + location.y - location.z) * 16
		projected = Vector2D(x, y);
		center    = self.projectCenter()
		return projected.sub(center)
		
	def projectCenter(self):
		x = (self.center.x - self.center.y) * 32
		y = (self.center.x + self.center.y - self.center.z) * 16
		return Vector2D(x,y)
		
		
	def pickTile(self, mouse_x, mouse_y):
		pass