import sys
import pygame


pygame.init()
pygame.display.set_caption("Keys")

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")
            print(f"The name of the key is: {pygame.key.name(event.key)}")

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
sys.exit()
