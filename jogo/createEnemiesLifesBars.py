import pygame

def createLifeBar(entityPosX, entityPosY, entityLife, screen):
    counter = 0
    if counter < 1:
        initialLife = entityLife
    else:
        counter+=1
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(entityPosX, entityPosY-30, initialLife*13, 20))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(entityPosX, entityPosY-30, initialLife*13 - entityLife*13, 20))