import sys, pygame
from sph import *

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
sim = FluidSimulation(640, 480)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			sim.addParticle(event.pos)

	deltaTime = clock.tick(60)
	sim.update(deltaTime)
	screen.fill((255, 255, 255))
	sim.display(screen)
	pygame.display.flip()
