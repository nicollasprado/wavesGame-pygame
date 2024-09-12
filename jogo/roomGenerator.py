import enemies, pygame

import enemies.angryBlock
import enemies.tankBlocks

class generateRooms():
    def __init__(self):
        self.totalEnemies = 0
        self.actualRoom = 0

    def spawnEnemies(self, enemiesSpriteList: pygame.sprite.Group):
        if(not enemiesSpriteList):
            for x in range(self.actualRoom*3):
                enemiesSpriteList.add(enemies.angryBlock.AngryBlock())
                self.totalEnemies += 1
            for y in range(int(self.actualRoom*1.5)):
                enemiesSpriteList.add(enemies.tankBlocks.TankBlocks())
                self.totalEnemies += 1
            self.actualRoom+=1