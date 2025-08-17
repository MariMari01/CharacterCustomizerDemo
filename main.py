# Example file showing a circle moving on screen
import pygame
import helper_functions as hf
import classes as cls



# pygame setup
pygame.init()
screen_width = 1020
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0

main_background = pygame.image.load("background_space.png").convert()
tile_width, tile_height = main_background.get_size()


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

nav_skin_shades = cls.Nav_button(10, 10, 200, 50, "Skin Shades", hf.skin_shades)
nav_back_hairs = cls.Nav_button(10, 10, 200, 50, "Back Hairs", hf.back_hairs)
nav_bangs = cls.Nav_button(10, 70, 200, 50, "Bangs", hf.bangs)
nav_ponytails = cls.Nav_button(10, 130, 200, 50, "Ponytails", hf.ponytails)
nav_sides = cls.Nav_button(10, 190, 200, 50, "Sides", hf.sides)
nav_brows = cls.Nav_button(10, 250, 200, 50, "Brows", hf.brows)
nav_eyes = cls.Nav_button(10, 310, 200, 50, "Eyes", hf.eyes)
nav_face_accessories = cls.Nav_button(10, 370, 200, 50, "Face Accessories", hf.face_accessories)
nav_noses = cls.Nav_button(10, 430, 200, 50, "Noses", hf.noses)
nav_mouths = cls.Nav_button(10, 490, 200, 50, "Mouths", hf.mouths)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(0, screen_width, tile_width):
        for y in range(0, screen_height, tile_height):
            screen.blit(main_background, (x, y))

    hf.display_image(screen, "character_creator_background.png")

    nav_skin_shades.draw(screen)
    hf.display_image(screen, "sketch.png")
    
    nav_back_hairs.draw(screen)
    nav_bangs.draw(screen)
    nav_ponytails.draw(screen)
    nav_sides.draw(screen)
    nav_brows.draw(screen)
    nav_eyes.draw(screen)
    nav_face_accessories.draw(screen)
    nav_noses.draw(screen)
    nav_mouths.draw(screen)
    
    pygame.display.flip()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


