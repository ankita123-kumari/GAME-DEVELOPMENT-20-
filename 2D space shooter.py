import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
player_img = pygame.image.load("spaceship.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Player settings
player_x, player_y = WIDTH // 2 - 25, HEIGHT - 80
player_speed = 5

# Enemy settings
enemies = [{"x": random.randint(0, WIDTH - 50), "y": random.randint(-100, -40)} for _ in range(5)]
enemy_speed = 3

# Bullet settings
bullets = []
bullet_speed = -7

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 20))  # Background color
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append({"x": player_x + 22, "y": player_y})

    # Bullet movement
    for bullet in bullets:
        bullet["y"] += bullet_speed

    # Enemy movement
    for enemy in enemies:
        enemy["y"] += enemy_speed
        if enemy["y"] > HEIGHT:
            enemy["y"] = random.randint(-100, -40)
            enemy["x"] = random.randint(0, WIDTH - 50)

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if enemy["x"] < bullet["x"] < enemy["x"] + 50 and enemy["y"] < bullet["y"] < enemy["y"] + 50:
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append({"x": random.randint(0, WIDTH - 50), "y": random.randint(-100, -40)})

    # Draw elements
    screen.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy["x"], enemy["y"]))
    for bullet in bullets:
        screen.blit(bullet_img, (bullet["x"], bullet["y"]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()