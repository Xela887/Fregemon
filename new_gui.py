from GameClass import GameClass
import Widgets
import tkinter as tk
import pygame


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.FPS = 20

        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        self.window_width = int(screen_width * 1)
        self.window_height = int(screen_height * 1)

        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Fregemon")

        self.game_manager = GameClass()
        
        self.current_screen = StartMenu(self, self.game_manager)

    def change_screen(self, new_screen):
        self.current_screen = new_screen

    def load_picture(self):
        front_bauz_img = pygame.image.load("pics/front_bauz_img.gif")
        self.front_bauz_img = pygame.transform.scale(front_bauz_img, (self.window_width * 0.1, self.window_height * 0.1))
        front_flamiau_img = pygame.image.load("pics/front_flamiau_img.gif")
        self.front_flamiau_img = pygame.transform.scale(front_flamiau_img, (self.window_width * 0.1, self.window_height * 0.1))
        front_robball_img = pygame.image.load("pics/front_robball_img.gif")
        self.front_robball_img = pygame.transform.scale(front_robball_img, (self.window_width * 0.1, self.window_height * 0.1))
        pokemon_battlesprite = pygame.image.load("pics/pokemon_battlesprite.png")
        self.pokemon_battlesprite = pygame.transform.scale(pokemon_battlesprite, (self.window_width * 1, self.window_height * 1))

    def start(self):
        running = True

        self.load_picture()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.current_screen.handle_events(event)

            self.current_screen.update()
            self.screen.blit(self.pokemon_battlesprite, (self.window_width * 0, self.window_height * 0))
            self.current_screen.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()


class Screen:
    def __init__(self, manager: Gui, game_manager: GameClass):
        self.manager = manager
        self.game_manager = game_manager

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


class StartMenu(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Fregemon", (manager.window_width // 2, manager.window_height * 0.3), 60, (255, 255, 255))

        self.play_button = Widgets.Button("Spielen", (manager.window_width * 0.45, manager.window_height * 0.50, manager.window_width * 0.10, manager.window_height * 0.05))
        self.play_button.set_action(self.play)
        self.quit_button = Widgets.Button("Quit", (manager.window_width * 0.45, manager.window_height * 0.60, manager.window_width * 0.10, manager.window_height * 0.05))
        self.quit_button.set_action(self.quit)

    def handle_events(self, event):
        self.play_button.handle_event(event)
        self.quit_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        self.play_button.draw(surface)
        self.quit_button.draw(surface)

    def play(self):
        self.manager.change_screen(GameSelection(self.manager, self.game_manager))

    def quit(self):
        pygame.quit()


class GameSelection(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

    def handle_events(self, event):
        pass
    
    def draw(self, surface):
        pass
