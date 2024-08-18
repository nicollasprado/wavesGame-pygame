import pygame, random, constants

class AngryBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('jogo/sprites/inimigo.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/angryBlock-damaged1.png'))
        self.sprites.append(pygame.image.load('jogo/sprites/angryBlock-damaged2.png'))
        self.actual = 0
        self.image = self.sprites[int(self.actual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(800, 1200), random.randint(160, 600))
        self.playerX = 0
        self.playerY = 0

        self.life = 5 * constants.chosenDifficulty
        self.strength = 1 * constants.chosenDifficulty
        self.speed = 1.5
        self.oldMovementTick = 0
        self.walkTimer = 0

    def update(self):
        self.chasePlayer()
        self.changeSpriteOnDamageTaken()

    def trackPlayer(self, playerX, playerY):
        self.playerX = playerX
        self.playerY = playerY

    def chasePlayer(self):
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

    def changeSpriteOnDamageTaken(self):
        if(self.life <= self.life/2 and self.life >= self.life/3):
            print(1)
            self.actual = 1
        if(self.life <= self.life/3 and self.life >= 0):
            self.actual = 2
        self.image = self.sprites[int(self.actual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))