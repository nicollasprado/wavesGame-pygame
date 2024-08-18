import pygame, playerC, mainAttack, firstRoomConfigs, createEnemiesLifesBars, constants

pygame.init()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Collector")
clock = pygame.time.Clock()
constants.chosenDifficulty = 2
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()


firstRoomOBJ = firstRoomConfigs.firstRoom()

player = playerC.Player()
mouseOneAttack = mainAttack.mainAttack()
allSprites.add([player, mouseOneAttack])

font = pygame.font.SysFont('arial', 40, True, False)
points = 0

def createAim(mouseX, mouseY):
    pygame.draw.line(screen, (0,255,255), (player.rect.x+25, player.rect.y+25), (mouseX, mouseY))
    pygame.draw.circle(screen, (0, 255, 255), (mouseX, mouseY), 10.0, 1)

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    cursor = pygame.mouse.get_pos()

    firstRoomOBJ.spawnEnemies(enemySprites)
    enemySprites.draw(screen)
    enemySprites.update()

    for enemy in enemySprites:
        createEnemiesLifesBars.createLifeBar(enemy.rect.x, enemy.rect.y, enemy.life, screen)
        enemy.trackPlayer(player.rect.x, player.rect.y)

    allSprites.draw(screen)
    allSprites.update()

    lifeUI = f'VIDA: {player.life}'
    lifeUI_formatted = font.render(lifeUI, True, (255, 255, 255))
    pointsUI = f"PONTOS: {points}"
    pointsUI_formatted = font.render(pointsUI, True, (255, 255, 255))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseOneAttack.triggerAtack == False):
            mouseOneAttack.attack(cursor[0], cursor[1])
        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            for enemy in enemySprites:
                if(enemy.rect.collidepoint(cursor)):
                    enemy.life -= 1
                    if(enemy.life <= 0):
                        enemy.kill()
                        enemy.rect.x = 100000
                        points += 1

    if(pygame.key.get_pressed()):
        player.walk()

    if(player.checkDamageCooldown(pygame.time.get_ticks())):
        for enemy in enemySprites:
            if(player.rect.colliderect(enemy.rect)):
                player.life -= 10
                player.lastDamageTick = pygame.time.get_ticks()

    createAim(cursor[0], cursor[1])

    screen.blit(lifeUI_formatted, (1090, 0))
    screen.blit(pointsUI_formatted, (1050, 50))
    pygame.display.flip()



pygame.quit()
