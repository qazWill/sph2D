import math


# used in summations 
# assigns weight to values by proximity
# r - neighboring particle's distance away
# h - maximum distance before receiving weight of 0
def generalSmoothing(r, h):
	if r >= h:
		return 0	
	else:
		return (315 * math.pow((h*h - r*r), 3)) / (64 * math.PI * math.pow(h, 9))




# used in summations for calculating pressure
# assigns weight to values by proximity
# r - neighboring particle's distance away
# h - maximum distance before receiving weight of 0
def pressureSmoothing(r, h):
	if r >= h:
		return 0	
	else:
		return (15 * math.pow((h - r), 3)) / (math.PI * math.pow(h, 6))
		



# used in summations for calculating viscocity
# assigns weight to values by proximity
# r - neighboring particle's distance away
# h - maximum distance before receiving weight of 0
def viscocitySmoothing(r, h):
	if r >= h:
		return 0	
	else:
		return -(r*r*r / (2*h*h*h)) + (r*r / (h*h)) + (h/(2*r)) - 1




class Particle:

	def __init__(self, pos, r, mass, density):

		self.pos = pos 
		self.radius = r
		self.mass = mass
		self.density = density


class Simulation:

	def __init__(self, width, height):

		self.width = width
		self.height = height
		self.particles = []

	def display(self, screen):
		for particle in self.particles:
			pygame.draw.circle(screen, (0, 0, 255), particle.pos, particle.radius)

	
