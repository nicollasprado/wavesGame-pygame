import angryBlock, tankBlocks, pygame

class firstRoom():
    def __init__(self):
        self.qtAngryBlocks = 10
        self.qtTankBlocks = 3
        self.qtSpeedBlocks = 2
        self.qtFollowerBlocks = 5
        self.qtEnragedBlocks = 1
        self.totalEnemies = 21
        self.totalEnemiesFirstWave = 10
        self.firstWaveAlreadySpawned = False
        self.totalEnemiesSecondWave = 10
        self.SecondWaveAlreadySpawned = False
        self.BossAlreadySpawned = False
        self.totalEnemies = 21
        self.counterFirstWave = 100
        self.counterSecondWave = 150
        self.counterBoss = 200

    def spawnEnemies(self, enemiesSpriteList: pygame.sprite.Group):
        if(self.firstWaveAlreadySpawned == False):
            for x in range(5):
                enemiesSpriteList.add(angryBlock.AngryBlock())
            for y in range(1):
                enemiesSpriteList.add(tankBlocks.TankBlocks())
            self.firstWaveAlreadySpawned = True
        if(self.firstWaveAlreadySpawned == True and self.SecondWaveAlreadySpawned == False and not enemiesSpriteList):
            for x in range(5):
                enemiesSpriteList.add(angryBlock.AngryBlock())
            for y in range(2):
                enemiesSpriteList.add(tankBlocks.TankBlocks())
            self.SecondWaveAlreadySpawned = True