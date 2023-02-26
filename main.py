import pygame

WIDTH, HEIGHT = 1500, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#Importing image assets
PATH_TO_ASSETS = 'assets/'
MAN_IN_CANNON_WIDTH, MAN_IN_CANNON_HEIGHT = 300, 200
CIRCUS_BACKGROUND_WIDTH, CIRCUS_BACKGROUND_HEIGHT = WIDTH, HEIGHT

MAN_IN_CANNON = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+'man_in_cannon_asset.png'), (MAN_IN_CANNON_WIDTH, MAN_IN_CANNON_HEIGHT))
CIRCUS_BACKGROUND = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+'circus_background_asset.jpg'), (CIRCUS_BACKGROUND_WIDTH, CIRCUS_BACKGROUND_HEIGHT))

#Game variables
x, y = 100, 600

#Game constants
FPS = 60
CLOCK = pygame.time.Clock()
BACKGROUND_COLOR = 255,255,255
GAME = True

#Main game loop
while GAME:
	CLOCK.tick(FPS)
	WINDOW.fill(BACKGROUND_COLOR)	

	WINDOW.blit(CIRCUS_BACKGROUND, (0,0))
	WINDOW.blit(MAN_IN_CANNON, (x, y))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME = False


	pygame.display.update()

