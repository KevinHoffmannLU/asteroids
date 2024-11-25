import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    if not SCREEN_HEIGHT or not SCREEN_WIDTH:
        raise Exception("Constants not imported")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.cotainers = (updatable, drawable)
    # I am not sure how to get the line above to work so I am doing it manually for now ! Check on this
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    updatable.add(player)
    drawable.add(player)
    
    print(updatable.sprites())
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000000)
        
        
        for update in updatable:
            update.update(dt)
            
        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        temp_dt = clock.tick(60)
        dt = temp_dt / 1000
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()