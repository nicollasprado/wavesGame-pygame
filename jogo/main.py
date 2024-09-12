import pygame, playerC, roomGenerator, createEnemiesLifesBars, constants, random
import mainAttack, spells.freeze
import ui.stats

class main():
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode(constants.screenSize)
        pygame.display.set_caption(constants.gameName)
        clock = pygame.time.Clock()
        constants.chosenDifficulty = 2
        allSprites = pygame.sprite.Group()
        enemySprites = pygame.sprite.Group()


        roomGen = roomGenerator.generateRooms()

        player = playerC.Player()
        mouseOneAttack = mainAttack.mainAttack()
        freezeSpell = spells.freeze.Freeze()
        allSprites.add([player, mouseOneAttack])

        points = 0
        stardust = 0

        def createAim(mouseX, mouseY):
            pygame.draw.line(screen, (0,255,255), (player.rect.x+25, player.rect.y+25), (mouseX, mouseY))
            pygame.draw.circle(screen, (0, 255, 255), (mouseX, mouseY), 10.0, 1)

        running = True
        while running:
            clock.tick(60)
            screen.fill((0, 0, 0))
            cursor = pygame.mouse.get_pos()

            roomGen.spawnEnemies(enemySprites)
            enemySprites.draw(screen)
            enemySprites.update()

            for enemy in enemySprites:
                createEnemiesLifesBars.createLifeBar(enemy.rect.x, enemy.rect.y, enemy.staticLife, enemy.life, screen)
                enemy.trackPlayer(player.rect.x, player.rect.y)

            allSprites.draw(screen)
            allSprites.update()

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
                                if(enemy.enemyType == 'AngryBlock'):
                                    stardust += random.randint(0, 1)
                                elif(enemy.enemyType == 'TankBlock'):
                                    stardust += random.randint(1, 2)

            if(pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s]):
                player.walk()

            if(freezeSpell.isFrozen and freezeSpell.checkFreezeTick(pygame.time.get_ticks())):
                freezeSpell.useFreeze(pygame.time.get_ticks(), enemySprites, stardust)
            if(pygame.key.get_pressed()[pygame.K_q]):
                stardust = freezeSpell.useFreeze(pygame.time.get_ticks(), enemySprites, stardust)
                

            if(player.checkDamageCooldown(pygame.time.get_ticks())):
                for enemy in enemySprites:
                    if(player.rect.colliderect(enemy.rect)):
                        player.life -= 10
                        player.lastDamageTick = pygame.time.get_ticks()
                    
            if(player.life == 0):
                main()

            createAim(cursor[0], cursor[1])

            ui.stats.createUI(player, points, stardust, screen)
            pygame.display.flip()



        pygame.quit()

if(__name__ == '__main__'):
    main()