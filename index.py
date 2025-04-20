<!DOCTYPE py>
<py>
# Begin by downloading pygame through command line terminal
# import pygame, time & random
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (253, 39, 3)
green = (0, 243, 61)
blue = (67, 94, 255)
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("CSC-221 Final Project - The Snake")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 13

font_style = pygame.font.SysFont("Cooper Black", 22)
score_font = pygame.font.SysFont("comicsansms", 33)

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, black, [block[0], block[1], snake_block, snake_block])
        
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    win.blit(value, [0, 0])
    
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])
    
def game_loop():
    game_over = False
    game_close = False
    
    x = width // 2
    y = height // 2

    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    food_x = random.randint(0, (width - snake_block) // 10) * 10
    food_y = random.randint(0, (height - snake_block) // 10) * 10

    while not game_over:

        while game_close:
            win.fill(white)
            message("Sorry You've Lost! Press C-Play Again or Q-Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()   

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = snake_block
                    dx = 0
        x += dx
        y += dy

        if x>= width or x < 0 or y >= height or y < 0:
            game_close = True

        win.fill(white)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randint(0, width - snake_block) / 10) * 10
            food_y = round(random.randint(0, height - snake_block) / 10) * 10
            length_of_snake += 1
            
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()
    
game_loop()
# Let's see if this thing works....
# In
# 3.....
# 2...........
# 1....................
</py>
