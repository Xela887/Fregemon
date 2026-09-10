from GameClass import GameClass
import Trainer_Klasse as Trainer
import Altar_Klasse
from Pokemon_Klassen import Bauz, Flamiau, Robball
from Angriff_Klassen import Rasierblatt, Fliegen, Feuerzahn, Einäschern, Wasserdüse, KalteDusche, Attacken
import Save_Load
import Widgets
import tkinter as tk
import pygame


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.running = True

        pygame.init()
        self.clock = pygame.time.Clock()
        self.FPS = 20

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 192, 255)
        self.GREEN = (37, 196, 37)
        self.GRAY = (100, 100, 100)

        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        self.window_width = int(screen_width * 1)
        self.window_height = int(screen_height * 1)

        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Fregemon")

        self.game_manager = GameClass(spieler=Trainer.Spieler("", [], None, []), altar=None)
        
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
        self.load_picture()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

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

        self.title = Widgets.Label("Fregemon", (manager.window_width // 2, manager.window_height * 0.3), 60, manager.WHITE)

        self.play_button = Widgets.Button("Spielen", (manager.window_width * 0.45, manager.window_height * 0.50, 
                                                      manager.window_width * 0.10, manager.window_height * 0.05))
        self.play_button.set_action(self.play)
        self.quit_button = Widgets.Button("Quit", (manager.window_width * 0.45, manager.window_height * 0.60, 
                                                   manager.window_width * 0.10, manager.window_height * 0.05))
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
        self.manager.running = False


class GameSelection(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Spielauswahl", (manager.window_width // 2, manager.window_height * 0.3), 60, manager.WHITE)

        self.new_player_button = Widgets.Button("Neuer Spieler", (manager.window_width * 0.40, manager.window_height * 0.40, 
                                                                  manager.window_width * 0.20, manager.window_height * 0.06))
        self.new_player_button.set_action(self.new_player)
        self.load_game_button = Widgets.Button("Spielstand laden", (manager.window_width * 0.40, manager.window_height * 0.50, 
                                                                    manager.window_width * 0.20, manager.window_height * 0.06))
        self.load_game_button.set_action(self.load_player)
        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.60, 
                                                     manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)

    def handle_events(self, event):
        self.new_player_button.handle_event(event)
        self.load_game_button.handle_event(event)
        self.back_button.handle_event(event)
    
    def draw(self, surface):
        self.title.draw(surface)

        self.new_player_button.draw(surface)
        self.load_game_button.draw(surface)
        self.back_button.draw(surface)

    def new_player(self):
        self.manager.change_screen(NewPlayer(self.manager, self.game_manager))

    def load_player(self):
        spieler, altar = Save_Load.load()
        if spieler == [] and altar == []:
            return
        self.game_manager = GameClass(spieler=spieler, altar=altar)
        self.manager.change_screen(MainMenu(self.manager, self.game_manager))

    def back(self):
        self.manager.change_screen(StartMenu(self.manager, self.game_manager))


class NewPlayer(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Neuer Spieler", (manager.window_width // 2, manager.window_height * 0.3), 60, manager.WHITE)

        self.name_input = Widgets.TextInput((manager.window_width * 0.35, manager.window_height * 0.40, 
                                             manager.window_width * 0.30, manager.window_height * 0.06))
        self.confirm_button = Widgets.Button("Bestätigen", (manager.window_width * 0.40, manager.window_height * 0.50, 
                                                            manager.window_width * 0.20, manager.window_height * 0.06))
        self.confirm_button.set_action(self.confirm_name)
        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.60, 
                                                     manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)

    def handle_events(self, event):
        self.name_input.handle_event(event)
        self.confirm_button.handle_event(event)
        self.back_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        self.name_input.draw(surface)
        self.confirm_button.draw(surface)
        self.back_button.draw(surface)

    def confirm_name(self):
        self.game_manager.spieler.name = self.name_input.text
        self.manager.change_screen(ChooseStarter(self.manager, self.game_manager))

    def back(self):
        self.manager.change_screen(GameSelection(self.manager, self.game_manager))


class ChooseStarter(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Wähle einen Starter", (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        self.choose_bauz_button = Widgets.Button("Bauz", (manager.window_width * 0.25, manager.window_height * 0.70, 
                                                          manager.window_width * 0.10, manager.window_height * 0.06))
        self.choose_bauz_button.set_action(self.choose_bauz)
        self.choose_flamiau_button = Widgets.Button("Flamiau", (manager.window_width * 0.45, manager.window_height * 0.70, 
                                                                manager.window_width * 0.10, manager.window_height * 0.06))
        self.choose_flamiau_button.set_action(self.choose_flamiau)
        self.choose_robball_button = Widgets.Button("Robball", (manager.window_width * 0.65, manager.window_height * 0.70, 
                                                                manager.window_width * 0.10, manager.window_height * 0.06))
        self.choose_robball_button.set_action(self.choose_robball)

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.80, 
                                                     manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)

        front_bauz_img = pygame.image.load("pics/front_bauz_img.gif")
        self.front_bauz_img = pygame.transform.scale(front_bauz_img, (manager.window_width * 0.1, manager.window_height * 0.1))
        front_flamiau_img = pygame.image.load("pics/front_flamiau_img.gif")
        self.front_flamiau_img = pygame.transform.scale(front_flamiau_img, (manager.window_width * 0.1, manager.window_height * 0.1))
        front_robball_img = pygame.image.load("pics/front_robball_img.gif")
        self.front_robball_img = pygame.transform.scale(front_robball_img, (manager.window_width * 0.1, manager.window_height * 0.1))

    def handle_events(self, event):
        self.choose_bauz_button.handle_event(event)
        self.choose_flamiau_button.handle_event(event)
        self.choose_robball_button.handle_event(event)
        self.back_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        pygame.draw.rect(surface, self.manager.GREEN,(self.manager.window_width * 0.225, self.manager.window_height * 0.30, 
                                                      self.manager.window_width * 0.15, self.manager.window_height * 0.475))
        pygame.draw.rect(surface, self.manager.RED,(self.manager.window_width * 0.425, self.manager.window_height * 0.30, 
                                                    self.manager.window_width * 0.15, self.manager.window_height * 0.475))
        pygame.draw.rect(surface, self.manager.BLUE,(self.manager.window_width * 0.625, self.manager.window_height * 0.30, 
                                                     self.manager.window_width * 0.15, self.manager.window_height * 0.475))

        self.choose_bauz_button.draw(surface)
        self.choose_flamiau_button.draw(surface)
        self.choose_robball_button.draw(surface)

        self.back_button.draw(surface)

        surface.blit(self.front_bauz_img, (self.manager.window_width * 0.25, self.manager.window_height * 0.50))
        surface.blit(self.front_flamiau_img, (self.manager.window_width * 0.45, self.manager.window_height * 0.50))
        surface.blit(self.front_robball_img, (self.manager.window_width * 0.65, self.manager.window_height * 0.50))

    def choose_bauz(self):
        starter_pokemon = Bauz(attacken=[Rasierblatt(), Fliegen()], fp=5)
        self.create_gameclass(starter_pokemon)

    def choose_flamiau(self):
        starter_pokemon = Flamiau(attacken=[Feuerzahn(), Einäschern()], fp=5)
        self.create_gameclass(starter_pokemon)

    def choose_robball(self):
        starter_pokemon = Robball(attacken=[Wasserdüse(), KalteDusche()], fp=5)
        self.create_gameclass(starter_pokemon)

    def create_gameclass(self, starter_pokemon):
        spieler = Trainer.Spieler(self.game_manager.spieler.name, [starter_pokemon], starter_pokemon, [starter_pokemon])
        altar = Altar_Klasse.Altar_For_Sacrifices(spieler, 0, 0, 0)
        self.game_manager.spieler = spieler
        self.game_manager.altar = altar
        self.manager.change_screen(MainMenu(self.manager, self.game_manager))

    def back(self):
        self.manager.change_screen(NewPlayer(self.manager, self.game_manager))


class MainMenu(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Hauptmenü", (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        self.fight_button = Widgets.Button("Kämpfen", (manager.window_width * 0.40,manager.window_height * 0.40, 
                                                       manager.window_width * 0.20,manager.window_height * 0.06))
        self.fight_button.set_action(self.fight)
        self.pokemon_button = Widgets.Button("Pokemon", (manager.window_width * 0.40,manager.window_height * 0.50, 
                                                         manager.window_width * 0.20,manager.window_height * 0.06))
        self.pokemon_button.set_action(self.pokemon)
        self.altar_button = Widgets.Button("Altar zum Opfern", (manager.window_width * 0.40,manager.window_height * 0.60, 
                                                                manager.window_width * 0.20,manager.window_height * 0.06))
        self.altar_button.set_action(self.altar)
        self.save_button = Widgets.Button("Speichern", (manager.window_width * 0.40,manager.window_height * 0.70, 
                                                        manager.window_width * 0.20,manager.window_height * 0.06))
        self.save_button.set_action(self.save)
        self.quit_button = Widgets.Button("Quit", (manager.window_width * 0.40,manager.window_height * 0.80, 
                                                   manager.window_width * 0.20,manager.window_height * 0.05))
        self.quit_button.set_action(self.ask_confirmation)

        self.show_confirmation = False
        self.confirm_quit_label = Widgets.Label("Hast du gespeichert?", (manager.window_width * 0.50, manager.window_height * 0.33), 60)
        self.confirm_quit_button = Widgets.Button("Ja", (manager.window_width * 0.375, manager.window_height * 0.36, 
                                                         manager.window_width * 0.25, manager.window_height * 0.04))
        self.confirm_quit_button.set_action(self.quit)
        self.cancel_quit_button = Widgets.Button("Nein", (manager.window_width * 0.375, manager.window_height * 0.41, 
                                                          manager.window_width * 0.25, manager.window_height * 0.14))
        self.cancel_quit_button.set_action(self.cancel_quit)

    def handle_events(self, event):
        if not self.show_confirmation:
            self.fight_button.handle_event(event)
            self.pokemon_button.handle_event(event)
        self.altar_button.handle_event(event)
        self.save_button.handle_event(event)
        self.quit_button.handle_event(event)

        self.confirm_quit_button.handle_event(event)
        self.cancel_quit_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        if not self.show_confirmation: 
            self.fight_button.draw(surface)
            self.pokemon_button.draw(surface)
        self.altar_button.draw(surface)
        self.save_button.draw(surface)
        self.quit_button.draw(surface)

        if self.show_confirmation:
            pygame.draw.rect(surface, self.manager.WHITE, 
                            (self.manager.window_width * 0.35, 
                             self.manager.window_height * 0.30, 
                             self.manager.window_width * 0.30, 
                             self.manager.window_height * 0.30))
            pygame.draw.rect(surface, self.manager.WHITE, 
                            (self.manager.window_width * 0.35, 
                             self.manager.window_height * 0.30, 
                             self.manager.window_width * 0.30, 
                             self.manager.window_height * 0.30),
                             width=3)
            self.confirm_quit_label.draw(surface)
            self.confirm_quit_button.draw(surface)
            self.cancel_quit_button.draw(surface)

    def fight(self):
        self.manager.change_screen(StartCombat(self.manager, self.game_manager))

    def pokemon(self):
        self.manager.change_screen(PokemonOverview(self.manager, self.game_manager))

    def altar(self):
        self.manager.change_screen(Altar(self.manager, self.game_manager))

    def save(self):
        Save_Load.save(self.game_manager.spieler.name, 
                       self.game_manager.spieler.pokemonliste, 
                       self.game_manager.altar, 
                       self.game_manager.spieler.pokemon_team)

    def ask_confirmation(self):
        self.show_confirmation = True

    def cancel_quit(self):
        self.show_confirmation = False

    def quit(self):
        self.manager.running = False


class StartCombat(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

    def handle_events(self, event):
        pass

    def draw(self, surface):
        pass


class PokemonOverview(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Pokemon", (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        self.view_pokemon_scrollbar = Widgets.PokemonScrollBar(self.game_manager.spieler.pokemonliste, 16)
        self.view_pokemon_scrollbar.start()

        self.team_editor_button = Widgets.Button("Team-Editor", (manager.window_width * 0.40, manager.window_height * 0.78, 
                                                                 manager.window_width * 0.20, manager.window_height * 0.06))

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.85, 
                                                     manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)

    def handle_events(self, event):
        self.team_editor_button.handle_event(event)
        self.back_button.handle_event(event)

        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
            for poke_name, btn in self.view_pokemon_stats_button_list:
                if btn.rect.collidepoint(mouse_pos):
                    self.selected_pokemon = next(p for p in self.game_manager.spieler.pokemonliste if p.name == poke_name)
                    self.game_manager.selected_pokemon = self.selected_pokemon
                    self.manager.change_screen(PokemonStats(self.manager, self.game_manager))

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.view_pokemon_scrollbar.scroll_up()
            elif event.y < 0:
                self.view_pokemon_scrollbar.scroll_down()

    def draw(self, surface):
        self.title.draw(surface)

        pokemonliste = [str(poke.name) for poke in self.view_pokemon_scrollbar.get_scrollbarliste()]
                
        self.view_pokemon_stats_button_list = []
        
        width_adder = 0.10
        height_adder = 0.30
        line_count = 0
        for poke in pokemonliste:
            if line_count == 4:
                line_count = 0
                height_adder += 0.10
                width_adder = 0.10
            btn = Widgets.Button(poke, (self.manager.window_width * width_adder, self.manager.window_height * height_adder, 
                                        self.manager.window_width * 0.18, self.manager.window_height * 0.06))
            self.view_pokemon_stats_button_list.append((poke, btn))
            width_adder += 0.20
            line_count += 1

        for btn in self.view_pokemon_stats_button_list:
            btn[1].draw(surface)

        self.team_editor_button.draw(surface)
        self.back_button.draw(surface)

        if self.view_pokemon_scrollbar.check_scrollable():
            self.view_pokemon_scrollbar.draw_scrollbar_indicator_frame(surface, self.manager.window_width, self.manager.window_height)
            self.view_pokemon_scrollbar.draw_scrollbar_indicator(surface, self.manager.window_width, self.manager.window_height)

    def back(self):
        self.manager.change_screen(MainMenu(self.manager, self.game_manager))


class PokemonStats(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label(str(game_manager.selected_pokemon.name), (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        self.fp_label = Widgets.Label(f"FP: {game_manager.selected_pokemon.fp}", (manager.window_width * 0.65, manager.window_height * 0.42), 60)
        self.zp_label = Widgets.Label(f"ZP: {game_manager.altar.fp_amount}", (manager.window_width * 0.65, manager.window_height * 0.38), 60)
        self.convert_zp_button = Widgets.Button("Convert", (manager.window_width * 0.55, manager.window_height * 0.363, 
                                                       manager.window_width * 0.06, manager.window_height * 0.03))
        self.convert_zp_button.set_action(self.convert_zp)

        self.level_label = Widgets.Label(f"Level: {self.game_manager.selected_pokemon.level}", (manager.window_width * 0.43, manager.window_height * 0.32), 60)
        self.ep_label = Widgets.Label(f"EP: {round(self.game_manager.selected_pokemon.ep, 2)}/{round(100 * self.game_manager.selected_pokemon.level ** 1.1, 2)}",
                                      (manager.window_width * 0.43, manager.window_height * 0.37), 60)
        self.type_label = Widgets.Label(f"Typ: {', '.join(self.game_manager.selected_pokemon.typ)}", (manager.window_width * 0.43, manager.window_height * 0.42), 60)
        self.kp_label = Widgets.Label(f"KP: {self.game_manager.selected_pokemon.maxkp}", (manager.window_width * 0.43, manager.window_height * 0.47), 60)
        self.atk_label = Widgets.Label(f"ATK: {self.game_manager.selected_pokemon.atk}", (manager.window_width * 0.43, manager.window_height * 0.52), 60)
        self.def_label = Widgets.Label(f"DEF: {self.game_manager.selected_pokemon.defence}", (manager.window_width * 0.43, manager.window_height * 0.57), 60)
        self.spatk_label = Widgets.Label(f"SPATK: {self.game_manager.selected_pokemon.spatk}", (manager.window_width * 0.43, manager.window_height * 0.62), 60)
        self.spdef_label = Widgets.Label(f"SPDEF: {self.game_manager.selected_pokemon.spdef}", (manager.window_width * 0.43, manager.window_height * 0.67), 60)
        self.init_label = Widgets.Label(f"INIT: {self.game_manager.selected_pokemon.init}", (manager.window_width * 0.43, manager.window_height * 0.72), 60)

        self.kp_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.46, 
                                                   manager.window_width * 0.02, manager.window_height * 0.03))
        self.kp_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.46, 
                                                    manager.window_width * 0.02, manager.window_height * 0.03))
        self.atk_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.51, 
                                                    manager.window_width * 0.02, manager.window_height * 0.03))
        self.atk_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.51, 
                                                     manager.window_width * 0.02, manager.window_height * 0.03))
        self.def_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.56, 
                                                    manager.window_width * 0.02, manager.window_height * 0.03))
        self.def_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.56, 
                                                     manager.window_width * 0.02, manager.window_height * 0.03))
        self.spatk_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.61, 
                                                      manager.window_width * 0.02, manager.window_height * 0.03))
        self.spatk_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.61, 
                                                       manager.window_width * 0.02, manager.window_height * 0.03))
        self.spdef_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.66, 
                                                      manager.window_width * 0.02, manager.window_height * 0.03))
        self.spdef_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.66, 
                                                       manager.window_width * 0.02, manager.window_height * 0.03))
        self.init_plus_button = Widgets.Button("+", (manager.window_width * 0.63, manager.window_height * 0.71, 
                                                     manager.window_width * 0.02, manager.window_height * 0.03))
        self.init_minus_button = Widgets.Button("-", (manager.window_width * 0.66, manager.window_height * 0.71, 
                                                      manager.window_width * 0.02, manager.window_height * 0.03))

        self.kp_plus_button.set_action(self.kp_plus)
        self.kp_minus_button.set_action(self.kp_minus)
        self.atk_plus_button.set_action(self.atk_plus)
        self.atk_minus_button.set_action(self.atk_minus)
        self.def_plus_button.set_action(self.def_plus)
        self.def_minus_button.set_action(self.def_minus)
        self.spatk_plus_button.set_action(self.spatk_plus)
        self.spatk_minus_button.set_action(self.spatk_minus)
        self.spdef_plus_button.set_action(self.spdef_plus)
        self.spdef_minus_button.set_action(self.spdef_minus)
        self.init_plus_button.set_action(self.init_plus)
        self.init_minus_button.set_action(self.init_minus)

        self.physical_attack_button = Widgets.Button(game_manager.selected_pokemon.attacken[0].__class__.__name__, 
                                                     (manager.window_width * 0.32, manager.window_height * 0.79, 
                                                     manager.window_width * 0.16, manager.window_height * 0.04))
        self.physical_attack_button.set_action(self.physical_attack)
        self.special_attack_button = Widgets.Button(game_manager.selected_pokemon.attacken[1].__class__.__name__,  
                                                    (manager.window_width * 0.52, manager.window_height * 0.79, 
                                                    manager.window_width * 0.16, manager.window_height * 0.04))
        self.special_attack_button.set_action(self.special_attack)
        self.evolve_button = Widgets.Button("Entwickeln", (manager.window_width * 0.52, manager.window_height * 0.74, 
                                                           manager.window_width * 0.16, manager.window_height * 0.04))
        self.evolve_button.set_action(self.evolve)

        if game_manager.selected_pokemon in game_manager.spieler.pokemon_team:
            self.plusorminus = "-"
        elif game_manager.selected_pokemon not in game_manager.spieler.pokemon_team:
            self.plusorminus = "+"
        self.add_to_team_button = Widgets.Button(f"{self.plusorminus} Team", (manager.window_width * 0.32, manager.window_height * 0.74, 
                                                                         manager.window_width * 0.16, manager.window_height * 0.04))
        self.add_to_team_button.set_action(self.add_to_team)

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.85, 
                                                     manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)

    def handle_events(self, event):
        self.convert_zp_button.handle_event(event)

        self.kp_plus_button.handle_event(event)
        self.kp_minus_button.handle_event(event)
        self.atk_plus_button.handle_event(event)
        self.atk_minus_button.handle_event(event)
        self.def_plus_button.handle_event(event)
        self.def_minus_button.handle_event(event)
        self.spatk_plus_button.handle_event(event)
        self.spatk_minus_button.handle_event(event)
        self.spdef_plus_button.handle_event(event)
        self.spdef_minus_button.handle_event(event)
        self.init_plus_button.handle_event(event)
        self.init_minus_button.handle_event(event)

        self.physical_attack_button.handle_event(event)
        self.special_attack_button.handle_event(event)
        self.evolve_button.handle_event(event)

        self.add_to_team_button.handle_event(event)

        self.back_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        pygame.draw.rect(surface, 
                                 self.manager.WHITE, 
                                (self.manager.window_width * 0.30, 
                                 self.manager.window_height * 0.29, 
                                 self.manager.window_width * 0.40, 
                                 self.manager.window_height * 0.55))
        pygame.draw.rect(surface, 
                                 self.manager.GRAY, 
                                (self.manager.window_width * 0.30, 
                                 self.manager.window_height * 0.29, 
                                 self.manager.window_width * 0.40, 
                                 self.manager.window_height * 0.55),
                                 width=3)

        self.fp_label.draw(surface)
        self.zp_label.draw(surface)
        self.convert_zp_button.draw(surface)

        self.level_label.draw(surface)
        self.ep_label.draw(surface)
        self.type_label.draw(surface)
        self.kp_label.draw(surface)
        self.atk_label.draw(surface)
        self.def_label.draw(surface)
        self.spatk_label.draw(surface)
        self.spdef_label.draw(surface)
        self.init_label.draw(surface)

        self.kp_plus_button.draw(surface)
        self.kp_minus_button.draw(surface)
        self.atk_plus_button.draw(surface)
        self.atk_minus_button.draw(surface)
        self.def_plus_button.draw(surface)
        self.def_minus_button.draw(surface)
        self.spatk_plus_button.draw(surface)
        self.spatk_minus_button.draw(surface)
        self.spdef_plus_button.draw(surface)
        self.spdef_minus_button.draw(surface)
        self.init_plus_button.draw(surface)
        self.init_minus_button.draw(surface)

        self.physical_attack_button.draw(surface)
        self.special_attack_button.draw(surface)
        if self.game_manager.evolution.check_evolution(self.game_manager.selected_pokemon) != None:
            self.evolve_button.draw(surface)

        if self.game_manager.selected_pokemon in self.game_manager.spieler.pokemon_team:
            self.plusorminus = "-"
        elif self.game_manager.selected_pokemon not in self.game_manager.spieler.pokemon_team:
            self.plusorminus = "+"
        self.add_to_team_button.text = f"{self.plusorminus} Team"
        self.add_to_team_button.draw(surface)

        self.back_button.draw(surface)

    def convert_zp(self):
        if self.game_manager.altar.fp_amount > 0:
            self.game_manager.altar.fp_amount -= 1
            self.game_manager.selected_pokemon.fp += 1

    def kp_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.maxkp += 1
            self.game_manager.selected_pokemon.fp -= 1

    def kp_minus(self):
        if self.game_manager.selected_pokemon.maxkp > self.game_manager.selected_pokemon.base_maxkp:
            self.game_manager.selected_pokemon.maxkp -= 1
            self.game_manager.selected_pokemon.fp += 1

    def atk_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.atk += 1
            self.game_manager.selected_pokemon.fp -= 1

    def atk_minus(self):
        if self.game_manager.selected_pokemon.atk > self.game_manager.selected_pokemon.base_atk:
            self.game_manager.selected_pokemon.atk -= 1
            self.game_manager.selected_pokemon.fp += 1

    def def_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.defence += 1
            self.game_manager.selected_pokemon.fp -= 1

    def def_minus(self):
        if self.game_manager.selected_pokemon.defence > self.game_manager.selected_pokemon.base_def:
            self.game_manager.selected_pokemon.defence -= 1
            self.game_manager.selected_pokemon.fp += 1

    def spatk_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.spatk += 1
            self.game_manager.selected_pokemon.fp -= 1

    def spatk_minus(self):
        if self.game_manager.selected_pokemon.spatk > self.game_manager.selected_pokemon.base_spatk:
            self.game_manager.selected_pokemon.spatk -= 1
            self.game_manager.selected_pokemon.fp += 1

    def spdef_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.spdef += 1
            self.game_manager.selected_pokemon.fp -= 1

    def spdef_minus(self):
        if self.game_manager.selected_pokemon.spdef > self.game_manager.selected_pokemon.base_spdef:
            self.game_manager.selected_pokemon.spdef -= 1
            self.game_manager.selected_pokemon.fp += 1

    def init_plus(self):
        if self.game_manager.selected_pokemon.fp > 0:
            self.game_manager.selected_pokemon.init += 1
            self.game_manager.selected_pokemon.fp -= 1

    def init_minus(self):
        if self.game_manager.selected_pokemon.init > self.game_manager.selected_pokemon.base_init:
            self.game_manager.selected_pokemon.init -= 1
            self.game_manager.selected_pokemon.fp += 1

    def physical_attack(self):
        self.manager.change_screen(ViewPhysicalAttack(self.manager, self.game_manager))

    def special_attack(self):
        self.manager.change_screen(ViewSpecialAttack(self.manager, self.game_manager))

    def evolve(self):
        self.game_manager.evolution.evolution(self.game_manager.selected_pokemon)

    def add_to_team(self):
        if len(self.game_manager.spieler.pokemon_team) < 6 and self.game_manager.selected_pokemon not in self.game_manager.spieler.pokemon_team:
            self.game_manager.spieler.pokemon_team.append(self.game_manager.selected_pokemon)
        else:
            if self.game_manager.selected_pokemon in self.game_manager.spieler.pokemon_team:
                self.game_manager.spieler.pokemon_team.remove(self.game_manager.selected_pokemon)

    def back(self):
        self.manager.change_screen(PokemonOverview(self.manager, self.game_manager))


class ViewPhysicalAttack(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label(str(game_manager.selected_pokemon.attacken[0].__class__.__name__), 
                                    (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        self.damage_label = Widgets.Label(f"Schaden: {game_manager.selected_pokemon.attacken[0].atkdmg}", 
                                            (manager.window_width * 0.50, manager.window_height * 0.37), 60)
        self.type_label = Widgets.Label(f"Typ: {game_manager.selected_pokemon.attacken[0].typ}", 
                                        (manager.window_width * 0.50, manager.window_height * 0.42), 60)
        self.attack_type_label = Widgets.Label(f"Attackentyp: {game_manager.selected_pokemon.attacken[0].dmgtype}", 
                                                (manager.window_width * 0.50, manager.window_height * 0.47), 60)
        self.change_cost_label = Widgets.Label(f"Kosten: {game_manager.altar.change_attack_cost} Besiegte Trainer", 
                                                (manager.window_width * 0.50, manager.window_height * 0.60), 60)
        self.change_attack_button = Widgets.Button("Wechseln", (manager.window_width * 0.42, manager.window_height * 0.65, 
                                                                manager.window_width * 0.16, manager.window_height * 0.04))
        self.change_attack_button.set_action(self.change_attack)

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.75, 
                                                        manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)
    
    def handle_events(self, event):
        self.change_attack_button.handle_event(event)

        self.back_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        pygame.draw.rect(surface, self.manager.WHITE, (self.manager.window_width * 0.33, self.manager.window_height * 0.29, 
                                                       self.manager.window_width * 0.34, self.manager.window_height * 0.45))
        pygame.draw.rect(surface, self.manager.GRAY, (self.manager.window_width * 0.33, self.manager.window_height * 0.29, 
                                                       self.manager.window_width * 0.34, self.manager.window_height * 0.45),
                                                       width=3)
        self.damage_label.draw(surface)
        self.type_label.draw(surface)
        self.attack_type_label.draw(surface)
        self.change_cost_label.draw(surface)
        self.change_attack_button.draw(surface)

        self.back_button.draw(surface)

    def change_attack(self):
        self.game_manager.altar.trainer_bodies -= self.game_manager.altar.change_attack_cost
        self.manager.change_screen(ChangePhysicalAttack(self.manager, self.game_manager))

    def back(self):
        self.manager.change_screen(PokemonStats(self.manager, self.game_manager))


class ChangePhysicalAttack(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Neue Attacke wählen", (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)

        alle_attacken = [cls() for cls in Attacken]
        
        gefilterte_attacken = []
        for attacke in alle_attacken:
            if (getattr(attacke, "dmgtype") == "physisch"
            and getattr(attacke, "typ") in game_manager.selected_pokemon.typ
            and attacke.__class__.__name__ != game_manager.selected_pokemon.attacken[0].__class__.__name__):
                gefilterte_attacken.append(attacke)

        attackenliste = [attacke for attacke in gefilterte_attacken]

        self.view_attacken_button_list = []

        width_adder = 0.10
        height_adder = 0.30
        line_count = 0
        for attacke in attackenliste:
            if line_count == 4:
                line_count = 0
                height_adder += 0.08
                width_adder = 0.10
            btn = Widgets.Button(
                attacke.__class__.__name__,
                (manager.window_width * width_adder,
                manager.window_height * height_adder,
                manager.window_width * 0.18,
                manager.window_height * 0.06)
            )
            self.view_attacken_button_list.append((attacke, btn))
            width_adder += 0.20
            line_count += 1

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.85, 
                                                        manager.window_width * 0.20,  manager.window_height * 0.06))
        self.back_button.set_action(self.back)
    
    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
            for attacke, btn in self.view_attacken_button_list:
                if btn.rect.collidepoint(mouse_pos):
                    selected_attack = next(a for a in Attacken if a.__name__ == attacke.__class__.__name__)
                    self.game_manager.selected_pokemon.attacken[0] = selected_attack()
                    self.manager.change_screen(ViewPhysicalAttack(self.manager, self.game_manager))

        self.back_button.handle_event(event)

    def draw(self, surface):
        for btn in self.view_attacken_button_list:
            btn[1].draw(surface)

        self.back_button.draw(surface)

    def back(self):
        self.game_manager.altar.trainer_bodies += self.game_manager.altar.change_attack_cost
        self.manager.change_screen(ChangePhysicalAttack(self.manager, self.game_manager))


class ViewSpecialAttack(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label(str(game_manager.selected_pokemon.attacken[1].__class__.__name__), 
                                            (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)
        
        self.damage_label = Widgets.Label(f"Schaden: {game_manager.selected_pokemon.attacken[1].atkdmg}", 
                                            (manager.window_width * 0.50, manager.window_height * 0.37), 60)
        self.type_label = Widgets.Label(f"Typ: {game_manager.selected_pokemon.attacken[1].typ}", 
                                        (manager.window_width * 0.50, manager.window_height * 0.42), 60)
        self.attack_type_label = Widgets.Label(f"Attackentyp: {game_manager.selected_pokemon.attacken[1].dmgtype}", 
                                                (manager.window_width * 0.50, manager.window_height * 0.47), 60)
        self.change_cost_label = Widgets.Label(f"Kosten: {game_manager.altar.change_attack_cost} Besiegte Trainer", 
                                                (manager.window_width * 0.50, manager.window_height * 0.60), 60)
        self.change_attack_button = Widgets.Button("Wechseln", (manager.window_width * 0.42, manager.window_height * 0.65, 
                                                                manager.window_width * 0.16, manager.window_height * 0.04))
        self.change_attack_button.set_action(self.change_attack)

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.75, 
                                                        manager.window_width * 0.20, manager.window_height * 0.06))
        self.back_button.set_action(self.back)
    
    def handle_events(self, event):
        self.change_attack_button.handle_event(event)

        self.back_button.handle_event(event)

    def draw(self, surface):
        self.title.draw(surface)

        pygame.draw.rect(surface, self.manager.WHITE, (self.manager.window_width * 0.33, self.manager.window_height * 0.29, 
                                                        self.manager.window_width * 0.34, self.manager.window_height * 0.45))
        pygame.draw.rect(surface, self.manager.GRAY, (self.manager.window_width * 0.33, self.manager.window_height * 0.29, 
                                                        self.manager.window_width * 0.34, self.manager.window_height * 0.45),
                                                        width=3)
        self.damage_label.draw(surface)
        self.type_label.draw(surface)
        self.attack_type_label.draw(surface)
        self.change_cost_label.draw(surface)
        self.change_attack_button.draw(surface)

        self.back_button.draw(surface)

    def change_attack(self):
        self.game_manager.altar.trainer_bodies -= self.game_manager.altar.change_attack_cost
        self.manager.change_screen(ChangeSpecialAttack(self.manager, self.game_manager))

    def back(self):
        self.manager.change_screen(PokemonStats(self.manager, self.game_manager))


class ChangeSpecialAttack(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title = Widgets.Label("Neue Attacke wählen", (manager.window_width // 2, manager.window_height * 0.2), 60, manager.WHITE)
        
        alle_attacken = [cls() for cls in Attacken]
        
        gefilterte_attacken = []
        for attacke in alle_attacken:
            if (getattr(attacke, "dmgtype") == "spezial"
            and getattr(attacke, "typ") in game_manager.selected_pokemon.typ
            and attacke.__class__.__name__ != game_manager.selected_pokemon.attacken[1].__class__.__name__):
                gefilterte_attacken.append(attacke)

        attackenliste = [attacke for attacke in gefilterte_attacken]

        self.view_attacken_button_list = []

        width_adder = 0.10
        height_adder = 0.30
        line_count = 0
        for attacke in attackenliste:
            if line_count == 4:
                line_count = 0
                height_adder += 0.08
                width_adder = 0.10
            btn = Widgets.Button(
                attacke.__class__.__name__,
                (manager.window_width * width_adder,
                manager.window_height * height_adder,
                manager.window_width * 0.18,
                manager.window_height * 0.06)
            )
            self.view_attacken_button_list.append((attacke, btn))
            width_adder += 0.20
            line_count += 1

        self.back_button = Widgets.Button("Zurück", (manager.window_width * 0.40, manager.window_height * 0.85, 
                                                        manager.window_width * 0.20,  manager.window_height * 0.06))
        self.back_button.set_action(self.back)
    
    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
            for attacke, btn in self.view_attacken_button_list:
                if btn.rect.collidepoint(mouse_pos):
                    selected_attack = next(a for a in Attacken if a.__name__ == attacke.__class__.__name__)
                    self.game_manager.selected_pokemon.attacken[1] = selected_attack()
                    self.manager.change_screen(ViewSpecialAttack(self.manager, self.game_manager))

        self.back_button.handle_event(event)

    def draw(self, surface):
        for btn in self.view_attacken_button_list:
            btn[1].draw(surface)

        self.back_button.draw(surface)

    def back(self):
        self.game_manager.altar.trainer_bodies += self.game_manager.altar.change_attack_cost
        self.manager.change_screen(ChangeSpecialAttack(self.manager, self.game_manager))


class Altar(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

    def handle_events(self, event):
        pass

    def draw(self, surface):
        pass

