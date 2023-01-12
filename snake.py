import pygame
import random
import time

snake_speed = 15
#game window width and height
window_x = 720
window_y = 480

#Defining colors
black = pygame.Color(102, 204 ,153)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(15, 82, 186)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(128, 128, 128)


#initializing pygame
pygame.init()

#initializing pygame window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
#FPS Controller
fps = pygame.time.Clock()

snake_position = [100, 60] #initialising snake position
# defining first 4 blocks of snake
# body
snake_body = [[100, 60],
            [80, 60],
            [60, 60],
            [40, 60]
            ]
fruit_position = [random.randrange(1, (window_x//20)) * 20,
                        random.randrange(1, (window_y//20)) * 20]
fruit_spawn = True
# setting default snake direction
# towards right
direction = 'RIGHT'
change_to = direction

#initial Score
score = 0

def show_sccore( color, font, size):
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    #display score
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('your Score is : ' + str(score), True, red)

    #create a rectagular object for the text surface
    game_over_rect = game_over_surface.get_rect()

    #setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    #draw gameover
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #after 2 seconds we will quit the program
    time.sleep(2)

    #deactivate pygame
    pygame.quit()

    #quit the program
    quit()
def makegrid():
    BlockSize = 20
    for x in range(window_x):
        for j in range(window_y):
            rect = pygame.Rect(x*BlockSize, j*BlockSize, BlockSize, BlockSize)
            pygame.draw.rect(game_window, grey, rect, 1)

while True:
    #handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
             pygame.quit()

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #moving the snake
    if direction == 'UP':
        snake_position[1] -= 20
    if direction == 'DOWN':
        snake_position[1] += 20
    if direction == 'LEFT':
        snake_position[0] -= 20
    if direction == 'RIGHT':
        snake_position[0] += 20

    #snake body growing mechanism
    #if fruits and snake collide then score will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        
        score += 10
        snake_speed += 5
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//20)) * 20,
                        random.randrange(1, (window_y//20)) * 20]
                
    fruit_spawn = True
    game_window.fill(black)
    #makegrid()
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 20, 20
        ))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 20, 20
    ))

    #gameover Conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 20:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 20:
        game_over()

    #touching snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    #displaying score in real time in game
    show_sccore(white, 'times new roman ', 20)
    
    #refresh game screen
    pygame.display.update()
    #fps/ refresh rate
    fps.tick(snake_speed)