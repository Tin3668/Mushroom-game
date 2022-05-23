import pygame, sys
pygame.init()

size = (960, 480)

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
floorImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/flooring/floor.png")
dirtImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/flooring/dirt.png")
# playerImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/characters/")

def main():
    for x in range(0, 960, 48): 
        screen.blit(floorImg,(x, 480-(48*2)))
        screen.blit(dirtImg, (x, 480-48))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()

            pygame.display.update()
        clock.tick(60)

if (__name__ == '__main__'):
    main()