import constants

class Freeze:
    def __init__(self):
        self.sdCost = 5 * constants.chosenDifficulty
        self.cooldown = 10000 * constants.chosenDifficulty
        self.freezeTime = 3000
        self.startTick = 0
        self.finishTick = self.startTick + self.freezeTime
        self.lastUseFinishTick = 0
        self.isFrozen = False
        self.newStardust = 0

    def useFreeze(self, tick: int, enemiesGroup, stardustQt: int):
        if(self.isFrozen == False and tick >= self.lastUseFinishTick and stardustQt >= self.sdCost):
            for enemy in enemiesGroup:
                enemy.speed = 0
            self.startTick = tick
            self.finishTick = self.startTick + self.freezeTime
            self.isFrozen = True
            self.newStardust = stardustQt - self.sdCost
            return self.newStardust
        elif(tick >= self.finishTick):
            for enemy in enemiesGroup:
                enemy.speed = enemy.staticSpeed
                self.isFrozen = False
                self.lastUseFinishTick = self.finishTick + self.cooldown
            return stardustQt
        else:
            return stardustQt

    def checkFreezeTick(self, tick: int) -> bool:
        if(tick >= self.finishTick):
            return True