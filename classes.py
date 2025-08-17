import pygame
import helper_functions as hf

class Nav_button:
    def __init__(self, x, y, width, height, text, img_folder):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = "grey"
        self.hover_color = "green"
        self.clicked_color = "black"
        self.font = pygame.font.SysFont('Times New Roman', 24)
        self.is_clicked = False
        self.index = 0
        self.img_folder = img_folder

    def draw(self, surface):
        current_color = self.color
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                current_color = self.clicked_color
                if not self.is_clicked:
                    self.is_clicked = True
                    self.index += 1
                    if 0 <= self.index < len(self.img_folder):
                        pass
                    else:
                        self.index = 0  # Reset to first image if out of bounds
            else:
                self.is_clicked = False

        pygame.draw.rect(surface, current_color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255)) # White text
        text_rect = text_surface.get_rect(center=self.rect.center)
        hf.display_image(surface, self.img_folder[self.index])
        surface.blit(text_surface, text_rect)



    def get_index(self):
        return self.index

    def reset_index(self):
        self.index = 0