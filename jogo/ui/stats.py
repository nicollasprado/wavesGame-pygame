import pygame


def createUI(player, points: int, stardust: int, screen) -> list:
    font = pygame.font.SysFont('arial', 40, True, False)

    lifeRatio = player.life / player.staticLife
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1090, 0, 200, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1090, 0, (200 * lifeRatio), 30))

    pointsUI = f"PONTOS: {points}"
    pointsUI_formatted = font.render(pointsUI, True, (255, 255, 255))
    stardustUI = f"Stardusts: {stardust}"
    stardustUI_formatted = font.render(stardustUI, True, (255, 255, 255))
    screen.blit(pointsUI_formatted, (1050, 50))
    screen.blit(stardustUI_formatted, (1040, 100))