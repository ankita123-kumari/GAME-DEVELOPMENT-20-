import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tower settings
tower = pygame.Rect(350, 250, 40, 40)
bullets = []
bullet_speed = 5

# Enemy settings
enemies = [{"x": 0, "y": random.randint(100, 500), "speed": 2} for _ in range(5)]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append({"x": tower.x + 20, "y": tower.y + 20})

    # Bullet movement
    for bullet in bullets:
        bullet["x"] += bullet_speed

    # Enemy movement
    for enemy in enemies:
        enemy["x"] += enemy["speed"]
    
    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if enemy["x"] < bullet["x"] < enemy["x"] + 40 and enemy["y"] < bullet["y"] < enemy["y"] + 40:
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append({"x": 0, "y": random.randint(100, 500), "speed": 2})

    # Draw elements
    pygame.draw.rect(screen, BLUE, tower)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet["x"], bullet["y"], 10, 10))
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, (enemy["x"], enemy["y"], 40, 40))

    pygame.display.update()
    clock.tick(30)

pygame.quit()