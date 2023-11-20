import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
PADDLE_MARGIN = 50
PADDLE_SPEED = 0.5

BALL_RADIUS = 30


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PONG Game")

    clock = pygame.time.Clock()

    running = True

    paddle_player1_y = 50
    paddle_player2_y = 50

    ball_x = SCREEN_WIDTH//2
    ball_y = SCREEN_HEIGHT//2

    ball_speed = 0.4

    ball_v = pygame.math.Vector2(2, 1)
    ball_v.scale_to_length(ball_speed)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            paddle_player1_y -= PADDLE_SPEED*dt
            if paddle_player1_y < 0:
                paddle_player1_y = 0
        if keys[pygame.K_y]:
            paddle_player1_y += PADDLE_SPEED*dt
            if paddle_player1_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
                paddle_player1_y = SCREEN_HEIGHT - PADDLE_HEIGHT
        if keys[pygame.K_k]:
            paddle_player2_y -= PADDLE_SPEED*dt
            if paddle_player2_y < 0:
                paddle_player2_y = 0
        if keys[pygame.K_m]:
            paddle_player2_y += PADDLE_SPEED*dt
            if paddle_player2_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
                paddle_player2_y = SCREEN_HEIGHT - PADDLE_HEIGHT

        ball_x += ball_v[0]*dt
        ball_y += ball_v[1]*dt

        if ball_x < PADDLE_MARGIN + PADDLE_WIDTH + BALL_RADIUS:
            if ball_y > paddle_player1_y and ball_y < paddle_player1_y + PADDLE_HEIGHT:
                ball_x = PADDLE_MARGIN + PADDLE_WIDTH + BALL_RADIUS
                ball_v[0] = -ball_v[0]
            else:
                print("Point for player 2")
                ball_speed += 0.1
                ball_v.scale_to_length(ball_speed)
                ball_x = SCREEN_WIDTH//2
                ball_y = SCREEN_HEIGHT//2
        if ball_x > SCREEN_WIDTH - PADDLE_MARGIN - PADDLE_WIDTH - BALL_RADIUS:
            if ball_y > paddle_player2_y and ball_y < paddle_player2_y + PADDLE_HEIGHT:
                ball_x = SCREEN_WIDTH - PADDLE_MARGIN - PADDLE_WIDTH - BALL_RADIUS
                ball_v[0] = -ball_v[0]
            else:
                print("Point for player 1")
                ball_speed += 0.1
                ball_v.scale_to_length(ball_speed)
                ball_x = SCREEN_WIDTH//2
                ball_y = SCREEN_HEIGHT//2

        if ball_y > SCREEN_HEIGHT-BALL_RADIUS:
            ball_y = SCREEN_HEIGHT-BALL_RADIUS
            ball_v[1] = - ball_v[1]
        if ball_y < BALL_RADIUS:
            ball_y = BALL_RADIUS
            ball_v[1] = -ball_v[1]

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (PADDLE_MARGIN, paddle_player1_y,
                                         PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE,
                         (SCREEN_WIDTH-PADDLE_MARGIN-PADDLE_WIDTH, paddle_player2_y,
                          PADDLE_WIDTH, PADDLE_HEIGHT))

        pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

        pygame.display.update()


if __name__ == "__main__":
    main()
