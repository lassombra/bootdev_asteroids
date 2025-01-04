import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        offset = self.velocity * dt
        self.position += offset
        if (self.position.x > SCREEN_WIDTH or self.position.x < 0 or
                self.position.y > SCREEN_HEIGHT or self.position.y < 0):
            self.kill()