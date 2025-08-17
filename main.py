# Example file showing a circle moving on screen
import pygame
import helper_functions as hf

# pygame setup
pygame.init()
screen_width = 1020
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

main_background = pygame.image.load("background_space.png").convert()
tile_width, tile_height = main_background.get_size()


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(0, screen_width, tile_width):
        for y in range(0, screen_height, tile_height):
            screen.blit(main_background, (x, y))

    pygame.draw.circle(screen, "red", player_pos, 40)


    hf.display_image(screen, "character_images/Back Hair/Bat Wings .png", (100, 100))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


