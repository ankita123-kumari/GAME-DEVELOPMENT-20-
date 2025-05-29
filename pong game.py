import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Paddle settings
paddle_width, paddle_height = 10, 80
player_paddle = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ai_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

paddle_speed = 5

# Ball settings
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_dx, ball_dy = 4, 4

# Score
player_score, ai_score = 0, 0
font = pygame.font.Font(None, 36)

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
    if keys[pygame.K_UP] and player_paddle.y > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.y < HEIGHT - paddle_height:
        player_paddle.y += paddle_speed

    # AI movement (simple tracking)
    if ai_paddle.y + paddle_height // 2 < ball.y:
        ai_paddle.y += paddle_speed
    elif ai_paddle.y + paddle_height // 2 > ball.y:
        ai_paddle.y -= paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.y <= 0 or ball.y >= HEIGHT - ball.height:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_dx *= -1

    # Scoring system
    if ball.x <= 0:
        ai_score += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    if ball.x >= WIDTH:
        player_score += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2

    # Draw elements
    pygame.draw.rect(screen, GREEN, player_paddle)
    pygame.draw.rect(screen, GREEN, ai_paddle)
    pygame.draw.ellipse(screen, RED, ball)

    # Display score
    score_text = font.render(f"{player_score} - {ai_score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH // 2 - 30, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()