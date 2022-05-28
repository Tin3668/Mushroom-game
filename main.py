from async_timeout import current_task
import pygame, sys, os
pygame.init()

size = (960, 480)

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
floorImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/flooring/floor.png")
dirtImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/flooring/dirt.png")

idle_ani=[
pygame.image.load('sprites/characters/idle ani/idle_animation1.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation2.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation3.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation4.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation5.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation6.png'),
pygame.image.load('sprites/characters/idle ani/idle_animation7.png')]

moving_ani=[
pygame.image.load('sprites/characters/moving ani/moving_animation1.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation2.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation3.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation4.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation5.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation6.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation7.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation8.png'),
pygame.image.load('sprites/characters/moving ani/moving_animation9.png')]

# playerImg = pygame.image.load("E:/Programming/code/python/pygame/firstGame/sprites/characters/")

def main():
    last_update = pygame.time.get_ticks()
    animation_cooldown = 60;
    frame=0;
    for x in range(0, 960, 48): 
        screen.blit(floorImg,(x, 480-(48*2)))
        screen.blit(dirtImg, (x, 480-48))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f or pygame.K_LEFT:
                    pass
                if event.key == pygame.K_s or pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_SPACE or pygame.K_UP:
                    pass

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame+=1
            last_update=current_time;
            if frame >= len(idle_ani):
                frame = 0;
            screen.blit(moving_ani[frame],(0,0))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()