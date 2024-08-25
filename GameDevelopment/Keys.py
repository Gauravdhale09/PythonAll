import pygame

# set mensuration
game_win = pygame.display.set_mode((1000, 500))

# set name
pygame.display.set_caption('Game Name')
#colours
white = "#92ba8d"
black = "#111210"
# set exit variable
Exit_game = False
#ser
# Initialize loop

while not Exit_game:
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            Exit_game = True

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                print(e, "Right key is pressed")
    game_win.fill(white)
    pygame.draw.rect(game_win, black, [])
    pygame.display.update()

pygame.quit()
quit()
