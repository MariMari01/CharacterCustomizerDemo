import pygame

back_hairs = [
    "character_images/Back Hair/Bat Wings .png",
    "character_images/Back Hair/Butterfly Braids.png",
    "character_images/Back Hair/Dreads Bob.png",
    "character_images/Back Hair/Fluffy Long.png",
    "character_images/Back Hair/Fluffy Short.png",
    "character_images/Back Hair/Layer 89.png",
    "character_images/Back Hair/Lob.png",
    "character_images/Back Hair/Long Afro .png",
    "character_images/Back Hair/Long Straight.png",
    "character_images/Back Hair/Mullet.png",
    "character_images/Back Hair/Short Afro .png",
    "character_images/Back Hair/Short Afro.png",
    "character_images/Back Hair/Short Wavy.png"
]

bangs = [
    "character_images/Bangs/Afro Bangs.png",
    "character_images/Bangs/Braid Bangs.png",
    "character_images/Bangs/Curly Bangs.png",
    "character_images/Bangs/Fluffed.png",
    "character_images/Bangs/Harsh Side Part .png",
    "character_images/Bangs/Middle Part.png",
    "character_images/Bangs/Pixie.png",
    "character_images/Bangs/Reverse V Bangs.png",
    "character_images/Bangs/Sexy Bangs.png",
    "character_images/Bangs/Sexy Dreads.png",
    "character_images/Bangs/Side Part Bangs.png",
    "character_images/Bangs/Slick Bangs.png",
    "character_images/Bangs/Slick Dreads.png",
    "character_images/Bangs/Split Bangs.png",
    "character_images/Bangs/Straight Bangs.png",
    "character_images/Bangs/V Bangs.png"
]
ponytails = [
    "character_images/Ponytails/Braid L.png",
    "character_images/Ponytails/Braid R.png",
    "character_images/Ponytails/Double Buns .png",
    "character_images/Ponytails/High Ponytail.png",
    "character_images/Ponytails/L Side Pony.png",
    "character_images/Ponytails/Layer 73.png",
    "character_images/Ponytails/Low Ponytail.png",
    "character_images/Ponytails/Puff .png",
    "character_images/Ponytails/R Side Pony.png",
    "character_images/Ponytails/Twin Puffs.png"
]
sides = [
    "character_images/Sides/1 Braid Side .png",
    "character_images/Sides/2 Braid Side.png",
    "character_images/Sides/Fluffy Side.png",
    "character_images/Sides/Hime Side.png",
    "character_images/Sides/Long Dreads Side.png",
    "character_images/Sides/Long Side.png",
    "character_images/Sides/Medium Side.png",
    "character_images/Sides/Rough Sides .png",
    "character_images/Sides/Short Curls Side.png",
    "character_images/Sides/Short Dreads Side .png"
]
brows = [
    "character_images/Brows/Diva Brows .png",
    "character_images/Brows/Fluffy Brows.png",
    "character_images/Brows/Medium Brows.png",
    "character_images/Brows/Puffy Eyebrows.png",
    "character_images/Brows/Sad Brows.png",
    "character_images/Brows/Straight Brows.png"
]
eyes = [
    "character_images/Eyes/Cheerful Eyes.png",
    "character_images/Eyes/Doe Eyes.png",
    "character_images/Eyes/Serious Eyes.png",
    "character_images/Eyes/Sexy Eyes.png"
]
face_accessories = [
    "character_images/Face Accessories/Circle Glasses.png",
    "character_images/Face Accessories/Freckles .png",
    "character_images/Face Accessories/Scar 1.png",
    "character_images/Face Accessories/Scar 2.png",
    "character_images/Face Accessories/Wrinkles 1.png",
    "character_images/Face Accessories/Wrinkles 2.png"
]
noses = [
    "character_images/Noses/Beak Nose.png",
    "character_images/Noses/Flat Nose .png",
    "character_images/Noses/Hook Nose.png",
    "character_images/Noses/Upturned Nose.png"
]
mouths = [
    "character_images/Mouths/Big Frown.png",
    "character_images/Mouths/Diva Lipstick.png",
    "character_images/Mouths/Kitty Mouth.png",
    "character_images/Mouths/Neutral Mouth.png",
    "character_images/Mouths/Pouty Mouth.png"
]



def display_image(screen, img_path, position):
    image = pygame.image.load(img_path).convert_alpha()
    screen.blit(image, position)
    pygame.display.flip()
    return