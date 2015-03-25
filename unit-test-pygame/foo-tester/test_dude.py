from unittest import TestCase
from main import Dude
import pygame

__author__ = 'Rodrigo'


class TestDude(TestCase):
    def test_draw(self):
        self.size = self.width, self.height = 640, 400
        screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        dude = Dude(screen, 100, 200, 50, 50)
        self.assertRaises(Exception, pygame.draw.rect,screen, dude.color, dude.rect)


    def test_move_right(self):
        self.size = self.width, self.height = 640, 400
        screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        dude = Dude(screen, 100, 200, 50, 50)
        self.assertRaises(Exception, dude.move_right)

    def test_move_left(self):
        self.size = self.width, self.height = 640, 400
        screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        dude = Dude(screen, 100, 200, 50, 50)
        self.assertRaises(Exception, dude.move_left)

    def test_reset(self):
        self.size = self.width, self.height = 640, 400
        screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        dude = Dude(screen, 100, 200, 50, 50)
        self.assertRaises(Exception, dude.reset)