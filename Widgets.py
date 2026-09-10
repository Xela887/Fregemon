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
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
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


class TextInput():
    def __init__(self, rect, active_input=False):
        self.rect = pygame.Rect(rect)
        self.text = ""
        self.active_input = active_input
        self.font = pygame.font.SysFont(None, 60)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
            if self.active_input:
                self.active_input = False
            else:
                self.active_input = True

        if event.type == pygame.KEYDOWN and self.active_input:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        if self.active_input:
            pygame.draw.rect(surface, (0, 192, 255), self.rect, 3)
        else:
            pygame.draw.rect(surface, (100, 100, 100), self.rect, 3)
        name_surface = self.font.render(self.text, True, (0, 0, 0))
        surface.blit(name_surface, (self.rect.x + 10, self.rect.y + 10))


class PokemonScrollBar:
    def __init__(self, pokemonliste, size):
        self.__pokemonliste = pokemonliste
        self.__scrollbarliste = []
        self.__size = size
        self.__start_index = 0

    def start(self):
        self.__scrollbarliste = []
        for i in range(self.__size):
            try:
                self.__scrollbarliste.append(self.__pokemonliste[i])
            except IndexError:
                break

    def check_scrollable(self):
        if len(self.__pokemonliste) > self.__size:
            return True
        else:
            return False
    
    def __can_scroll_down(self):
        return self.__start_index + 4 < len(self.__pokemonliste)

    def scroll_down(self):
        if self.check_scrollable() and self.__can_scroll_down():
            self.__update_list_down()

    def __update_list_down(self):
        self.__start_index += 4
        self.__scrollbarliste = []
        for i in range(self.__size):
            try:
                self.__scrollbarliste.append(self.__pokemonliste[i + self.__start_index])
            except IndexError:
                break

    def scroll_up(self):
        if self.check_scrollable() and self.__start_index != 0:
            self.__update_list_up()

    def __update_list_up(self):
        self.__start_index -= 4
        self.__scrollbarliste = []
        for i in range(self.__size):
            try:
                self.__scrollbarliste.append(self.__pokemonliste[i + self.__start_index])
            except IndexError:
                break
    
    def get_scrollbarliste(self):
        return self.__scrollbarliste
    
    def draw_scrollbar_indicator_frame(self, surface, window_width, window_height):
        rect = pygame.Rect(window_width * 0.89, window_height * 0.30, window_width * 0.01, window_height * 0.36)
        pygame.draw.rect(surface, (255, 255, 255), rect)
        pygame.draw.rect(surface, (100, 100, 100), rect, 3)

    def draw_scrollbar_indicator(self, surface, window_width, window_height):
        lines = ((len(self.__pokemonliste) - self.__size) // 4) + 5
        spaces = (window_height * 0.36) / lines
        indicator_position = spaces * (self.__start_index / 4)
        rect = pygame.Rect(window_width * 0.89, window_height * 0.30 + indicator_position, window_width * 0.01, spaces)
        pygame.draw.rect(surface, (100, 100, 100), rect)

