import pygame
import time
import math
pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_image = pygame.image.load("clock.png")
clock_image = pygame.transform.scale(clock_image, (400, 400))

minute_hand = pygame.image.load("min_hand.png")
minute_hand = pygame.transform.scale(minute_hand, (400, 400))

second_hand = pygame.image.load("sec_hand.png")
second_hand = pygame.transform.scale(second_hand, (400, 400))

center_x, center_y = WIDTH//2, HEIGHT//2

def rotate_hands(image, angle, pivot, position):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_image, (50, 50))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle =  - (minutes * 6)
    second_angle =  - (seconds * 6)

    rotate_hands(minute_hand, minute_angle, (center_x, center_y), (center_x, center_y))
    rotate_hands(second_hand, second_angle, (center_x, center_y), (center_x, center_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()