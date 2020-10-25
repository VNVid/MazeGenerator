import auxiliary_functions
import pygame

pygame.init()


def update_win(win):
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1050, 20, 200, 30))
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1050, 70, 200, 30))
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1050, 120, 200, 30))
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render('Generate with DFS', 1, auxiliary_functions.BLACK)
    win.blit(text1, (1055, 30))
    text2 = f1.render('Generate with Prim', 1, auxiliary_functions.BLACK)
    win.blit(text2, (1055, 80))
    text3 = f1.render('Find path', 1, auxiliary_functions.BLACK)
    win.blit(text3, (1100, 130))
    text4 = f1.render('Size:', 1, auxiliary_functions.BLACK)
    win.blit(text4, (1055, 180))
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1130, 170, 30, 30))
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1170, 170, 40, 30))
    pygame.draw.rect(win, auxiliary_functions.LIGHTBLUE, (1220, 170, 30, 30))
    text5 = f1.render(str(auxiliary_functions.MAZE_SIZE), 1, auxiliary_functions.BLACK)
    win.blit(text5, (1178, 180))
    pygame.draw.polygon(win, auxiliary_functions.MAROON, [(1140, 180), (1150, 180), (1145, 190)])
    pygame.draw.polygon(win, auxiliary_functions.MAROON, [(1230, 190), (1240, 190), (1235, 180)])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
