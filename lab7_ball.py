import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_x, ball_y = WIDTH//2, HEIGHT//2
ball_speed = 20 

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_speed - ball_radius >= 0:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN and ball_y + ball_speed + ball_radius <= HEIGHT:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT and ball_x - ball_speed - ball_radius >= 0:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_x + ball_speed + ball_radius <= WIDTH:
                ball_x += ball_speed
    
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()