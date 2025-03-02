import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, red, [x[0], x[1], block_size, block_size])

def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [width / 2, height / 2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(black)
        message("You lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -block_size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = block_size
                x1_change = 0
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True
gameLoop()