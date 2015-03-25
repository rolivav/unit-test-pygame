__author__ = 'Rodrigo'

import pygame
from pymongo import MongoClient


class SaveDb:
    host = None
    client = None
    number_clients = 0

    @classmethod
    def init(cls, host):
        cls.host = host

    @classmethod
    def open_connection(cls):
        try:
            if cls.client is None:
                cls.number_clients += 1
                cls.client = MongoClient(cls.host)
        except Exception as ex:
            print "Error " + ex

    @classmethod
    def close_connection(cls):
        if cls.client is not None and cls.number_clients == 0:
            cls.client.close()
            cls.client = None
        else:
            cls.number_clients -= 1
    @classmethod
    def save_dude_state(cls, dude):
        cls.open_connection()
        db = cls.client['save_state']
        db.update_one({'_id': 0}, {'x': dude.x}, {'y': dude.y})
        cls.close_connection()

class Dude:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.rect = pygame.Rect((x, y), (w, h))
        self.color = (140, 240, 130)
        self.state = "STANDING"
        self.jumping_height = 500
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + w, self.y + h)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move_right(self):
        self.x += 0.1
        # self.rect = pygame.Rect((self.x, self.y), (self.w, self.h))

    def move_left(self):
        self.x -= 0.1
        # self.rect = pygame.Rect((self.x, self.y), (self.w, self.h))

    def jump(self):
        if self.state is "JUMPING":
            if self.jumping_height > 0:
                self.y -= 0.3
                self.jumping_height -= 1
            else:
                self.state = "FALLING"
        else:
            if self.state is "FALLING":
                if self.jumping_height < 500:
                    self.jumping_height += 1
                    self.y += 0.3
                else:
                    self.state = "STANDING"

        self.rect = pygame.Rect((self.x, self.y), (self.w, self.h))

    def reset(self):
        self. x = 100
        self.rect = pygame.Rect((self.x, self.y), (self.w, self.h))


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.dude = None
        self.size = self.width, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.dude = Dude(self.screen, 100, 200, 50, 50)

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.dude.jump()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.dude.move_right()
        if key[pygame.K_LEFT]:
            self.dude.move_left()
        if key[pygame.K_UP]:
            self.dude.reset()
        if key[pygame.K_SPACE]:
            if self.dude.state is "STANDING":
                self.dude.state = "JUMPING"
        pass

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.dude.draw()
        pygame.display.update()
        pass

    def on_cleanup(self):
        #SaveDb.save_dude_state(self.dude)
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    SaveDb.init("localhost")
    theApp = App()
    theApp.on_execute()