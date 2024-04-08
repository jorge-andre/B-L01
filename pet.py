import pygame

class Pet(pygame.sprite.Sprite):

    def __init__(self, pos=(0,0), speed=2):
        pygame.sprite.Sprite(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.pos = pos
        self.speed = speed
        self.happiness = 0
        self.age = 0