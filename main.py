import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    if not SCREEN_HEIGHT or not SCREEN_WIDTH:
        raise Exception("Constants not imported")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.cotainers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    # I am not sure how to get the line above to work so I am doing it manually for now ! Check on this
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    updatable.add(player)
    drawable.add(player)
    
    print(updatable.sprites())
    
    while True:
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000000)
        
        
        for update in updatable:
            update.update(dt)
            
        for draw in drawable:
            draw.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return
        
        pygame.display.flip()
        temp_dt = clock.tick(60)
        dt = temp_dt / 1000
    
if __name__ == "__main__":
    main()