# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        screen.fill((0, 0, 0))
        for updatable_entity in updatable:
            updatable_entity.update(dt)
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                pygame.quit()
                print ("Game over!")
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()