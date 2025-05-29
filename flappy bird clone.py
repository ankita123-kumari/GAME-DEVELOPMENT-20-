import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)

# Bird settings
bird_x, bird_y = 50, HEIGHT // 2
bird_radius = 15
gravity = 0.4
velocity = 0

# Pipe settings
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []

def create_pipe():
    pipe_height = random.randint(100, 300)
    pipes.append({"x": WIDTH, "height": pipe_height})

# Game variables
running = True
score = 0
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -7  # Jump

    # Bird movement
    velocity += gravity
    bird_y += velocity

    # Pipe movement & generation
    if len(pipes) == 0 or pipes[-1]["x"] < WIDTH - 200:
        create_pipe()
    
    for pipe in pipes:
        pipe["x"] -= pipe_speed
        pygame.draw.rect(screen, (0, 255, 0), (pipe["x"], 0, pipe_width, pipe["height"]))
        pygame.draw.rect(screen, (0, 255, 0), (pipe["x"], pipe["height"] + pipe_gap, pipe_width, HEIGHT))

        # Collision detection
        if bird_x + bird_radius > pipe["x"] and bird_x - bird_radius < pipe["x"] + pipe_width:
            if bird_y - bird_radius < pipe["height"] or bird_y + bird_radius > pipe["height"] + pipe_gap:
                running = False

    # Draw bird
    pygame.draw.circle(screen, (255, 0, 0), (bird_x, bird_y), bird_radius)

    # Game over if bird touches ground
    if bird_y + bird_radius > HEIGHT:
        running = False

    # Update screen
    pygame.display.update()
    clock.tick(30)

pygame.quit()