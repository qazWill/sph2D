import sys, pygame

screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()	

    screen.fill((255, 255, 255))
    pygame.display.flip()
