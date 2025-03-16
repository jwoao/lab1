import pygame

pygame.init()
pygame.mixer.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
cover_image = pygame.image.load("cover.jpeg")
cover_image = pygame.transform.scale(cover_image, (400, 400))

playlist = ["amygdala.mp3", "alexandria.mp3", "jericho.mp3"]
current_song = 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

running = True
play_music()

while running:
    screen.fill((0, 0, 0))
    screen.blit(cover_image, (50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(playlist)
                play_music()

    pygame.display.flip()
pygame.quit()