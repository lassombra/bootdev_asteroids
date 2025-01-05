# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids, drawable, shots, updatable = setup_groups()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    running = True
    while running:
        running, dt = game_loop(asteroids, clock, drawable, dt, player, screen, shots, updatable)


def game_loop(asteroids, clock, drawable, dt, player, screen, shots, updatable):
    screen.fill((0, 0, 0))
    for updatable_entity in updatable:
        updatable_entity.update(dt)
    for drawable_sprite in drawable:
        drawable_sprite.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False, dt
    for shot in shots:
        for asteroid in asteroids:
            if shot.collides_with(asteroid):
                asteroid.split()
                shot.kill()
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            print("Game over!")
            pygame.quit()
            return False, dt
    dt = clock.tick(60) / 1000
    return True, dt


def setup_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    return asteroids, drawable, shots, updatable


if __name__ == "__main__":
    main()