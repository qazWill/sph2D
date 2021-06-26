import math, pygame

def distance(a, b):
	return math.sqrt(math.pow(a[0]-b[0], 2), math.pow(a[1] - b[1], 2))

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
def flowSmoothing(r, h):
	if r >= h:
		return 0	
	else:
		return -(r*r*r / (2*h*h*h)) + (r*r / (h*h)) + (h/(2*r)) - 1




class Particle:

	def __init__(self, pos, r, mass):

		self.pos = pos 
		self.vel = [0, 0]
		self.radius = r
		self.mass = mass
		self.density = 0 
		self.pressure = 0


class FluidSimulation:

	def __init__(self, width, height):

		self.width = width
		self.height = height
		self.particles = []

		# simulation constants
		self.smoothingDist = 60
		self.restDensity = 0.008
		self.k = 1

	def addParticle(self, pos):
		self.particles.append(Particle(pos, 6, 1,))

	def display(self, screen):
		for particle in self.particles:
			pygame.draw.circle(screen, (0, 0, 255), particle.pos, particle.radius)

	def update(self, deltaTime):


		# recalculate pressure and density first since they are used in other formulas 
		for particle in particles:

			# density
			particle.density = 0
			for other in particles:
				if particle == other:
					continue
				particle.density += other.mass * generalSmoothing(distance(particle.pos, other.pos), self.smoothingDist)

			# pressure
			particle.pressure = self.k * (particle.density - self.restDensity)

		# recalculate forces, acceleration, and velocities
		for particle in particles
		
			# distance is used in most of the following calculations		
			r = distance(particle.pos, other.pos)
		
			# calculate pressure force
			pressureForce = [0, 0]
			for other in particles:
				if particle == other:
					continue
				magnitude = other.mass * (particle.pressure + other.pressure) / other.density
				magnitude *= pressureSmoothing(r, self.smoothingDist)
				direction = particle.pos
				direction[0] -= other.pos[0]
				direction[1] -= other.pos[1]
				direction[0] /= r
				direction[1] / = r
				pressureForce[0] += direction[0] * magnitude
				pressureForce[1] += direction[1] * magnitude


			# calculate flow force
			flowForce = [0, 0]
			for other in particles:
				if particle == other:
					continue	
				deltaForce = [0, 0]
				delta[0] = (other.vel[0] - particle.vel[0]) / other.density
				delta[1] = (other.vel[1] - particle.vel[1]) / other.density
				delta[0] *= flowSmoothing(r, self.smoothingDist) # this could be wrong!
				delta[1] *= flowSmoothing(r, self.smoothingDist) # this could be wrong!
				flowForce[0] += delta[0]
				flowForce[1] += delta[1]
				


			# calculate surface tension force
			surfaceTensiionForce = [0, 0]
				
					
			# calculate force from wall collisions		
			

			# sum forces and calculate new velocities
			totalForce = [0, 0] 
			totalForce[0] = pressureForce[0] + flowForce[0] + surfaceTensionForce[0]
			totalForce[1] = pressureForce[1] + flowForce[1] + surfaceTensionForce[1]
			accel = [0, 0]
			accel[0] = totalForce[0] / particle.density
			accel[1] = totalForce[1] / particle.density
			particle.vel[0] += accel[0] * deltaTime
			particle.vel[1] += accel[1] * deltaTime
					
	
















