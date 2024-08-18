import pygame

class mainAttack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('jogo/sprites/beam5.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/beam4.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/beam3.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/beam2.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/beam1.png'))
        self.actual = 0
        self.image = self.sprites[int(self.actual)]
        #self.image = pygame.transform.scale(self.image)
        self.rect = self.image.get_rect()

        self.rect.center = 1000, 1000
        self.triggerAtack = False

    def attack(self, mouseX, mouseY):
        self.rect.center = mouseX, mouseY
        self.triggerAtack = True

    def update(self):
        if(self.triggerAtack == True):
            self.actual += 0.25
            if(self.actual >= len(self.sprites)):
                self.actual = 0
                self.rect.center = 1000, 1000
                self.triggerAtack = False
            self.image = self.sprites[int(self.actual)]