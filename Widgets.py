import pygame


class Label:
    def __init__(self, text, position, font_size=40, color=(0, 0, 0)):
        self.text = text
        self.position = position
        self.color = color

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(
            self.text,
            True,
            self.color
        )

        self.rect = self.image.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class ShowLabel:
    def __init__(self, text, rect, font_size=40, color=(0, 0, 0), frame_color=(0, 0, 0)):
        self.text = text
        self.position = (rect[0], rect[1])
        self.color = color
        self.frame_color = frame_color

        self.label_rect = pygame.Rect(rect[0] - (rect[2]/2), rect[1] - (rect[3]/2), rect[2], rect[3])

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(
            self.text,
            True,
            self.color
        )

        self.rect = self.image.get_rect(center=(rect[0], rect[1]))

    def draw(self, surface):
        self.image = self.font.render(
            self.text,
            True,
            self.color
        )
        text_rect = self.image.get_rect(
            center=self.rect.center
        )
        pygame.draw.rect(surface, self.frame_color, self.label_rect, 2, 20)
        surface.blit(self.image, text_rect)

class Button:
    def __init__(self, text, rect, color=(255, 255, 255), hover_color=(171, 171, 171), text_color=(0, 0, 0), font_size=40, frame_color=(100, 100, 100), action_locked=False):
        self.text = text
        self.rect = pygame.Rect(rect)

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.frame_color = frame_color
        self.action_locked = action_locked

        self.font = pygame.font.Font(None, font_size)

        self.action = None

    def set_action(self, action):
        self.action = action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):

                if self.action and self.action_locked == False:
                    self.action()

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        # Hover-Effekt
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.rect(
            surface,
            color,
            self.rect
        )

        pygame.draw.rect(
            surface,
            self.frame_color,
            self.rect,
            3
        )

        text_image = self.font.render(
            self.text,
            True,
            self.text_color
        )

        text_rect = text_image.get_rect(
            center=self.rect.center
        )

        surface.blit(
            text_image,
            text_rect
        )