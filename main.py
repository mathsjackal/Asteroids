import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Creating Groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    Shot.containers = (shots,updatable,drawable)
    dt = 0
    # After setting up
    #print(f"Updatable group has {len(updatable)} sprites")
    #print(f"Drawable group has {len(drawable)} sprites")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for items in drawable:
            items.draw(screen)
        #updatable.update(dt)
        updatable.update(dt)

        for objects in asteroids:
            if objects.collision(player) == True:
                print("Game over!")
                #pygame.quit()
                sys.exit()
            for bullets in shots:
                if bullets.collision(objects) == True:
                    new_asteroids = objects.split()
                    if new_asteroids:
                        for new_asteroid in new_asteroids:
                            asteroids.add(new_asteroid)
                            updatable.add(new_asteroid)
                            drawable.add(new_asteroid)
                    bullets.kill()

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()