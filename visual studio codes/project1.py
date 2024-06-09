import pygame
pygame.init()
# display
x_state = 900
y_state = 600
fps = 60
screen = pygame.display.set_mode([x_state,y_state])
# variable names
# for colors we use RGB method 
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
exit_game = False
game_over = False
time = pygame.time.Clock()
def draw_catch_object(x_posi,y_posi):
    object1 = pygame.draw.circle(screen,black,(13,14),12)
# game loop 
while not exit_game:
    time.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    catch_object = draw_catch_object(x_state,y_state)
    screen.fill(white)
    pygame.display.flip()
pygame.quit()
quit()

