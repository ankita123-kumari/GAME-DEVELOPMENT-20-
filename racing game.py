import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Car settings
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
speed = 5

# Obstacles
obstacle_width = 50
obstacle_height = 100
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -100
obstacle_speed = 5

clock = pygame.time.Clock()
running = True

# Main loop
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += speed

    # Move obstacles
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -100
        obstacle_x = random.randint(0, WIDTH - obstacle_width)

    # Collision detection
    if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and \
       car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        print("Game Over!")
        running = False

    # Draw objects
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.update()
    clock.tick(30)

pygame.quit()