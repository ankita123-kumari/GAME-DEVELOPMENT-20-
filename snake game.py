import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
BLOCK_SIZE = 20
snake = [(100, 100)]
snake_dir = (BLOCK_SIZE, 0)
food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE, 
        random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)

clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN:
                snake_dir = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT:
                snake_dir = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                snake_dir = (BLOCK_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collision
    if new_head == food:
        food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE, 
                random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()

    if new_head in snake[1:] or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False

    # Draw elements
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    clock.tick(10)

pygame.quit()