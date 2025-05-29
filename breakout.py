import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle settings
paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 10)
paddle_speed = 6

# Ball settings
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2, 20, 20)
ball_dx, ball_dy = 4, -4

# Brick settings
brick_width, brick_height = 50, 20
bricks = [pygame.Rect(x, y, brick_width, brick_height) for x in range(50, WIDTH - 50, brick_width + 10) for y in range(50, 150, brick_height + 10)]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.x < WIDTH - paddle.width:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.x <= 0 or ball.x >= WIDTH - ball.width:
        ball_dx *= -1
    if ball.y <= 0:
        ball_dy *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Game over condition
    if ball.y >= HEIGHT:
        running = False

    # Draw elements
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, (0, 255, 0), brick)

    pygame.display.update()
    clock.tick(30)

pygame.quit()