import pygame

def createLifeBar(entityPosX, entityPosY, totalLife, entityLife, screen):
    ratio = entityLife / totalLife
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(entityPosX, entityPosY-30, 70, 20))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(entityPosX, entityPosY-30, (70 * ratio), 20))