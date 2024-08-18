import pygame, random, constants

class TankBlocks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('jogo/sprites/tank.png'))
        self.actual = 0
        self.image = self.sprites[int(self.actual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(800, 1200), random.randint(160, 600))
        self.playerX = 0
        self.playerY = 0

        self.life = 10 * constants.chosenDifficulty
        self.strength = 0.5 * constants.chosenDifficulty
        self.speed = 0.8
        self.oldMovementTick = 0
        self.walkTimer = 0

    def trackPlayer(self, playerX, playerY):
        self.playerX = playerX
        self.playerY = playerY

    def update(self):
        self.actual += 0.025
        if(self.actual >= len(self.sprites)):
            self.actual = 0
        if(self.actual >= 2):
            self.actual = 0
        self.image = self.sprites[int(self.actual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

        if(self.rect.x != self.playerX):
            if(self.rect.x < self.playerX):
                self.rect.x += self.speed*random.randint(1, 2)
            elif(self.rect.x > self.playerX):
                self.rect.x -= self.speed*random.randint(1, 2)
        if(self.rect.y != self.playerY):
            if(self.rect.y < self.playerY):
                self.rect.y += self.speed*random.randint(1, 2)
            elif(self.rect.y > self.playerY):
                self.rect.y -= self.speed*random.randint(1, 2)