from Angriff_Klassen import *
from Pokemon_Klassen import *
from Battle_Klasse import Battle
from Balancer_Klasse import Balancer
from Pokemon_Entwickeln import Evolution
from Trainer_Klasse import Spieler, Enemy
from Altar_Klasse import Altar_For_Sacrifices, zufalls_attacke, filter_pokemon_by_level, get_average_stat
from Save_Load import save, load
import tkinter as tk
import random
import pygame
import sys



def start_gui():
    FPS = 20

    evolution = Evolution()

    root = tk.Tk()
    root.withdraw()

    pygame.init()
    clock = pygame.time.Clock()

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    window_width = int(screen_width * 1)
    window_height = int(screen_height * 1)

    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Fregemon")

    BLACK = '#000000'
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)
    RED = (255, 0, 0)
    BLUE = (0, 192, 255)
    GREEN = (37, 196, 37)

    front_bauz_img = pygame.image.load("pics/front_bauz_img.gif")
    front_bauz_img = pygame.transform.scale(front_bauz_img, (window_width * 0.1, window_height * 0.1))
    front_flamiau_img = pygame.image.load("pics/front_flamiau_img.gif")
    front_flamiau_img = pygame.transform.scale(front_flamiau_img, (window_width * 0.1, window_height * 0.1))
    front_robball_img = pygame.image.load("pics/front_robball_img.gif")
    front_robball_img = pygame.transform.scale(front_robball_img, (window_width * 0.1, window_height * 0.1))
    pokemon_battlesprite = pygame.image.load("pics/pokemon_battlesprite.png")
    pokemon_battlesprite = pygame.transform.scale(pokemon_battlesprite, (window_width * 1, window_height * 1))

    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 40)
    smaller_font = pygame.font.SysFont(None, 30)

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
        
        def draw_scrollbar_indicator_frame(self):
            rect = pygame.Rect(window_width * 0.89, window_height * 0.30, window_width * 0.01, window_height * 0.36)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 3)

        def draw_scrollbar_indicator(self):
            lines = ((len(self.__pokemonliste) - self.__size) // 4) + 5
            spaces = (window_height * 0.36) / lines
            indicator_position = spaces * (self.__start_index / 4)
            rect = pygame.Rect(window_width * 0.89, window_height * 0.30 + indicator_position, window_width * 0.01, spaces)
            pygame.draw.rect(screen, GRAY, rect)

    def draw_button(text, x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, GRAY, rect, 3)
        text_surf = small_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)
        return rect

    class TeamSlotBox:
        def __init__(self, x, y, w, h):
            self.__color = BLACK
            self.__rect = pygame.Rect(x, y, w, h)
            self.text = ""

        def set_color(self, new_color):
            self.__color = new_color

        def draw(self):
            self.box = pygame.draw.rect(screen, self.__color, self.__rect, 4)
            self.__text_surf = small_font.render(self.text, True, BLACK)
            self.__text_rect = self.__text_surf.get_rect(center=self.__rect.center)
            screen.blit(self.__text_surf, self.__text_rect)


    first_slot = TeamSlotBox(window_width * 0.21, window_height * 0.68, window_height * 0.15, window_height * 0.15)
    second_slot = TeamSlotBox(window_width * 0.31, window_height * 0.68, window_height * 0.15, window_height * 0.15)
    third_slot = TeamSlotBox(window_width * 0.41, window_height * 0.68, window_height * 0.15, window_height * 0.15)
    fourth_slot = TeamSlotBox(window_width * 0.51, window_height * 0.68, window_height * 0.15, window_height * 0.15)
    fifth_slot = TeamSlotBox(window_width * 0.61, window_height * 0.68, window_height * 0.15, window_height * 0.15)
    sixth_slot = TeamSlotBox(window_width * 0.71, window_height * 0.68, window_height * 0.15, window_height * 0.15)

    blue_box = first_slot
    blue_box.set_color(BLUE)

    box_team_number = {
        first_slot : 0,
        second_slot : 1,
        third_slot : 2,
        fourth_slot : 3,
        fifth_slot : 4,
        sixth_slot : 5
    }

    def draw_text(text, x, y, color=(255, 255, 255)):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(x, y))
        screen.blit(surf, rect)

    def load_front_img(pokemon):
        img = pokemon.front_img
        if img == None:
            return
        full_img = "pics/" + img + ".gif"
        front_img = pygame.image.load(full_img)
        front_img = pygame.transform.scale(front_img, (window_width * 0.2, window_height * 0.2))
        screen.blit(front_img, (window_width * 0.70, window_height * 0.15))

    def load_back_img(pokemon):
        img = pokemon.back_img
        if img == None:
            return
        full_img = "pics/" + img + ".gif"
        back_img = pygame.image.load(full_img)
        back_img = pygame.transform.scale(back_img, (window_width * 0.2, window_height * 0.2))
        screen.blit(back_img, (window_width * 0.10, window_height * 0.55))



    input_box = pygame.Rect(window_width * 0.35, window_height * 0.40, window_width * 0.30, window_height * 0.06)
    player_name = ""
    active_input = False
    show_confirm_quit = False
    confirm_quit_button = None
    cancel_quit_button = None

    menu_state = "start_menu"

    selected_pokemon = None
    battle = None
    view_pokemon_stats_button_list = []


    running = True
    while running:
        clock.tick(FPS)
        screen.blit(pokemon_battlesprite, (window_width * 0, window_height * 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False):
                mouse_pos = event.pos

                # Startmenü
                if menu_state == "start_menu":
                    if play_button.collidepoint(mouse_pos):
                        menu_state = "game_selection"
                    elif quit_button.collidepoint(mouse_pos):
                        running = False

                # Spielauswahl
                elif menu_state == "game_selection":
                    if new_player_button.collidepoint(mouse_pos):
                        menu_state = "new_player"
                    elif load_game_button.collidepoint(mouse_pos):
                        spieler, altar = load(Attacken)
                        if spieler == [] and altar == []:
                            menu_state = "game_selection"
                        else:
                            menu_state = "main_menu"
                    elif back_button.collidepoint(mouse_pos):
                        menu_state = "start_menu"

                # Neuer Spieler
                elif menu_state == "new_player":
                    if input_box.collidepoint(mouse_pos):
                        active_input = True
                    else:
                        active_input = False
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "game_selection"
                    elif confirm_button.collidepoint(mouse_pos):
                        menu_state = "choose_starter"

                # Starter wählen
                elif menu_state == "choose_starter":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "game_selection"
                    elif choose_bauz_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                        starter_pokemon = Bauz(attacken=[Rasierblatt(), Fliegen()], fp=5)
                        spieler = Spieler(player_name, [starter_pokemon], starter_pokemon, [starter_pokemon])
                        altar = Altar_For_Sacrifices(spieler, 0, 0, 0)
                    elif choose_flamiau_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                        starter_pokemon = Flamiau(attacken=[Feuerzahn(), Flammenwurf()], fp=5)
                        spieler = Spieler(player_name, [starter_pokemon], starter_pokemon, [starter_pokemon])
                        altar = Altar_For_Sacrifices(spieler, 0, 0, 0)
                    elif choose_robball_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                        starter_pokemon = Robball(attacken=[Wasserdüse(), KalteDusche()], fp=5)
                        spieler = Spieler(player_name, [starter_pokemon], starter_pokemon, [starter_pokemon])
                        altar = Altar_For_Sacrifices(spieler, 0, 0, 0)


                # Hauptmenü
                elif menu_state == "main_menu":
                    enemys = ["Team Fregen Rüpel", "Nick Fregen"]
                    enemy_text = random.choices(enemys, weights=[99, 1], k=1)[0]
                    if save_button.collidepoint(mouse_pos):
                        save(spieler.name, spieler.pokemonliste, altar, spieler.pokemon_team)
                    elif start_combat_button.collidepoint(mouse_pos):
                        menu_state = "start_combat"
                    elif view_pokemon_button.collidepoint(mouse_pos):
                        menu_state = "view_pokemon"
                        view_pokemon_scrollbar = PokemonScrollBar(spieler.pokemonliste, 16)
                        view_pokemon_scrollbar.start()
                    elif altar_for_sacrifices_button.collidepoint(mouse_pos):
                        menu_state = "altar_for_sacrifices"
                        continue
                    elif quit_button.collidepoint(mouse_pos):
                        show_confirm_quit = True
                    elif show_confirm_quit == True:
                        if confirm_quit_button.collidepoint(mouse_pos):
                            running = False
                        elif cancel_quit_button.collidepoint(mouse_pos):
                            show_confirm_quit = False

                # Kampf annehmen
                elif menu_state == "start_combat":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                    elif accept_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 0:
                        menu_state = "combat_menu"
                        balancer = Balancer(all_pokemon, spieler.pokemon_team, Attacken)
                        balanced_enemy_team = balancer.make_balanced_enemy_team(len(spieler.pokemon_team))
                        enemy = Enemy(enemy_text, balanced_enemy_team, balanced_enemy_team[0], balanced_enemy_team)
                        battle = Battle(spieler.pokemon_team[0], spieler.pokemon_team, None, enemy.active_pokemon, enemy.pokemon_team, altar)

                # Kampf Aktion wählen
                elif menu_state == "combat_menu":
                    if fight_button.collidepoint(mouse_pos):
                        menu_state = "choose_attack"
                    elif swap_pokemon_button.collidepoint(mouse_pos):
                        menu_state = "swap_pokemon"

                # Kampf Attacke wählen
                elif menu_state == "choose_attack":
                    if attack1_button.collidepoint(mouse_pos):
                        menu_state = "combat_menu"
                        log = battle.player_attack_physic()
                        if log == "game_over_player":
                            menu_state = "fight_overview"
                        elif log == "game_over_enemy":
                            menu_state = "fight_overview"
                            altar.trainer_bodies += 1
                    elif attack2_button.collidepoint(mouse_pos):
                        menu_state = "combat_menu"
                        log = battle.player_attack_special()
                        if log == "game_over_player":
                            menu_state = "fight_overview"
                        elif log == "game_over_enemy":
                            menu_state = "fight_overview"
                            altar.trainer_bodies += 1
                    elif changed_my_mind_button.collidepoint(mouse_pos):
                        menu_state = "combat_menu"

                # Kampf Pokemon wechseln
                elif menu_state == "swap_pokemon":
                    if len(battle.spieler_poke_team) > 1:
                        if pokemon1_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 1:
                            battle.swap_pokemon_in_battle(1)
                            menu_state = "combat_menu"
                    if len(battle.spieler_poke_team) > 2:
                        if pokemon2_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 2:
                            battle.swap_pokemon_in_battle(2)
                            menu_state = "combat_menu"
                    if len(battle.spieler_poke_team) > 3:
                        if pokemon3_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 3:
                            battle.swap_pokemon_in_battle(3)
                            menu_state = "combat_menu"
                    if len(battle.spieler_poke_team) > 4:
                        if pokemon4_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 4:
                            battle.swap_pokemon_in_battle(4)
                            menu_state = "combat_menu"
                    if len(battle.spieler_poke_team) > 5:
                        if pokemon5_button.collidepoint(mouse_pos) and len(spieler.pokemon_team) > 5:
                            battle.swap_pokemon_in_battle(5)
                            menu_state = "combat_menu"
                    elif changed_my_mind_button.collidepoint(mouse_pos):
                        menu_state = "combat_menu"

                # Kampfergebnisse
                elif menu_state == "fight_overview":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                        battle.reset_player_team()

                # Pokemon
                elif menu_state == "view_pokemon":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                    elif team_editor_button.collidepoint(mouse_pos):
                        menu_state = "team_editor"
                        team_editor_scrollbar = PokemonScrollBar(spieler.pokemonliste, 16)
                        team_editor_scrollbar.start()
                    elif view_pokemon_stats_button_list:
                        for poke_name, btn in view_pokemon_stats_button_list:
                            if btn.collidepoint(mouse_pos):
                                selected_pokemon = next(p for p in spieler.pokemonliste if p.name == poke_name)
                                menu_state = "pokemon_stats"
                
                # Team Editor
                elif menu_state == "team_editor":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "view_pokemon"
                    elif view_pokemon_stats_button_list:
                        for poke_name, btn in view_pokemon_stats_button_list:
                            if btn.collidepoint(mouse_pos):
                                pokemon_added = False
                                selected_pokemon = next(p for p in spieler.pokemonliste if p.name == poke_name)
                                if not selected_pokemon in spieler.pokemon_team:
                                    try:
                                        spieler.pokemon_team[box_team_number[blue_box]] = selected_pokemon
                                        pokemon_added = True
                                    except IndexError:
                                        spieler.pokemon_team.append(selected_pokemon)
                                        pokemon_added = True
                                try:
                                    if selected_pokemon == spieler.pokemon_team[box_team_number[blue_box]] and pokemon_added == False:
                                        spieler.pokemon_team.remove(selected_pokemon)
                                        blue_box.text = ""
                                except IndexError:
                                    pass
                    if first_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        first_slot.set_color(BLUE)
                        blue_box = first_slot
                    if second_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        second_slot.set_color(BLUE)
                        blue_box = second_slot
                    if third_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        third_slot.set_color(BLUE)
                        blue_box = third_slot
                    if fourth_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        fourth_slot.set_color(BLUE)
                        blue_box = fourth_slot
                    if fifth_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        fifth_slot.set_color(BLUE)
                        blue_box = fifth_slot
                    if sixth_slot.box.collidepoint(mouse_pos):
                        blue_box.set_color(BLACK)
                        sixth_slot.set_color(BLUE)
                        blue_box = sixth_slot

                # Pokemon Stats
                elif menu_state == "pokemon_stats":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "view_pokemon"
                    if add_pokemon_to_team_button.collidepoint(mouse_pos):
                        if len(spieler.pokemon_team) < 6 and selected_pokemon not in spieler.pokemon_team:
                            spieler.pokemon_team.append(selected_pokemon)
                        else:
                            if selected_pokemon in spieler.pokemon_team:
                                spieler.pokemon_team.remove(selected_pokemon)
                    if physical_attack_button.collidepoint(mouse_pos):
                        menu_state = "view_physical_attack"
                    if special_attack_button.collidepoint(mouse_pos):
                        menu_state = "view_special_attack"
                    if add_fp_to_pokemon_button.collidepoint(mouse_pos):
                        if altar.fp_amount > 0:
                            altar.fp_amount -= 1
                            selected_pokemon.fp += 1
                    if evolution.check_evolution(selected_pokemon) != None:
                        if evolution_button.collidepoint(mouse_pos):
                            evolution.evolution(selected_pokemon)

                    # KP
                    if pokemon_view_kp_plus_button and pokemon_view_kp_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.maxkp += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_kp_minus_button and pokemon_view_kp_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.maxkp > selected_pokemon.base_maxkp:
                            selected_pokemon.maxkp -= 1
                            selected_pokemon.fp += 1

                    # ATK
                    if pokemon_view_atk_plus_button and pokemon_view_atk_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.atk += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_atk_minus_button and pokemon_view_atk_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.atk > selected_pokemon.base_atk:
                            selected_pokemon.atk -= 1
                            selected_pokemon.fp += 1

                    # DEF
                    if pokemon_view_def_plus_button and pokemon_view_def_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.defence += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_def_minus_button and pokemon_view_def_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.defence > selected_pokemon.base_def:
                            selected_pokemon.defence -= 1
                            selected_pokemon.fp += 1

                    # SPATK
                    if pokemon_view_spatk_plus_button and pokemon_view_spatk_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.spatk += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_spatk_minus_button and pokemon_view_spatk_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.spatk > selected_pokemon.base_spatk:
                            selected_pokemon.spatk -= 1
                            selected_pokemon.fp += 1

                    # SPDEF
                    if pokemon_view_spdef_plus_button and pokemon_view_spdef_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.spdef += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_spdef_minus_button and pokemon_view_spdef_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.spdef > selected_pokemon.base_spdef:
                            selected_pokemon.spdef -= 1
                            selected_pokemon.fp += 1

                    # INIT
                    if pokemon_view_init_plus_button and pokemon_view_init_plus_button.collidepoint(mouse_pos):
                        if selected_pokemon.fp > 0:
                            selected_pokemon.init += 1
                            selected_pokemon.fp -= 1

                    if pokemon_view_init_minus_button and pokemon_view_init_minus_button.collidepoint(mouse_pos):
                        if selected_pokemon.init > selected_pokemon.base_init:
                            selected_pokemon.init -= 1
                            selected_pokemon.fp += 1

                # Physische Attacke ansehen
                elif menu_state == "view_physical_attack":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "pokemon_stats"
                    if choose_attack_button.collidepoint(mouse_pos) and altar.trainer_bodies >= altar.change_attack_cost:
                        menu_state = "choose_new_physical_attack"
                        altar.trainer_bodies -= altar.change_attack_cost
                        
                # Neue Physische Attacke wählen
                elif menu_state == "choose_new_physical_attack":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "view_physical_attack"
                        altar.trainer_bodies += altar.change_attack_cost
                    elif view_attacken_button_list:
                        for attacke, btn in view_attacken_button_list:
                            if btn.collidepoint(mouse_pos):
                                selected_attack = next(a for a in Attacken if a.__name__ == attacke.__class__.__name__)
                                selected_pokemon.attacken[0] = selected_attack()
                                menu_state = "view_physical_attack"

                # Spezial Attacke ansehen
                elif menu_state == "view_special_attack":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "pokemon_stats"
                    if choose_attack_button.collidepoint(mouse_pos) and altar.trainer_bodies >= altar.change_attack_cost:
                        menu_state = "choose_new_special_attack"
                        altar.trainer_bodies -= altar.change_attack_cost

                # Neue Spezial Attacke wählen
                elif menu_state == "choose_new_special_attack":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "view_special_attack"
                        altar.trainer_bodies += altar.change_attack_cost
                    elif view_attacken_button_list:
                        for attacke, btn in view_attacken_button_list:
                            if btn.collidepoint(mouse_pos):
                                selected_attack = next(a for a in Attacken if a.__name__ == attacke.__class__.__name__)
                                selected_pokemon.attacken[1] = selected_attack()
                                menu_state = "view_special_attack"

                # Altar zum Opfern
                elif menu_state == "altar_for_sacrifices":
                    if back_button.collidepoint(mouse_pos):
                        menu_state = "main_menu"
                    elif sacrifice_for_pokemon_button.collidepoint(mouse_pos):
                        altar.sacrifice_for_pokemon()
                    elif sacrifice_for_fp_button.collidepoint(mouse_pos):
                        altar.sacrifice_for_fp()

            # Namen für neuen Spieler bestätigen
            elif event.type == pygame.KEYDOWN and active_input:
                if event.key == pygame.K_RETURN:
                    menu_state = "choose_starter"
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

            # Mausrad zum scrollen in einigen screens
            elif event.type == pygame.MOUSEWHEEL:
                if menu_state == "view_pokemon":
                    if event.y > 0:
                        view_pokemon_scrollbar.scroll_up()
                    elif event.y < 0:
                        view_pokemon_scrollbar.scroll_down()
                
                elif menu_state == "team_editor":
                    if event.y > 0:
                        team_editor_scrollbar.scroll_up()
                    elif event.y <0:
                        team_editor_scrollbar.scroll_down()

        # Startmenü
        if menu_state == "start_menu":
            title = font.render("Fregemon", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.3))

            play_button = draw_button("Spielen", window_width * 0.45, window_height * 0.50, window_width * 0.10, window_height * 0.05)
            quit_button = draw_button("Quit", window_width * 0.45, window_height * 0.60, window_width * 0.10, window_height * 0.05)

        # Spielauswahl
        elif menu_state == "game_selection":
            title = font.render("Spielauswahl", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            new_player_button = draw_button("Neuer Spieler", window_width * 0.40, window_height * 0.40, window_width * 0.20, window_height * 0.06)
            load_game_button = draw_button("Spielstand laden", window_width * 0.40, window_height * 0.50, window_width * 0.20, window_height * 0.06)
            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.60, window_width * 0.20, window_height * 0.06)

        # Neuer Spieler
        elif menu_state == "new_player":
            title = font.render("Neuer Spieler", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            pygame.draw.rect(screen, WHITE, input_box)
            pygame.draw.rect(screen, GRAY, input_box, 3)
            name_surface = small_font.render(player_name, True, BLACK)
            screen.blit(name_surface, (input_box.x + 10, input_box.y + 10))

            confirm_button = draw_button("Bestätigen", window_width * 0.40, window_height * 0.50, window_width * 0.20, window_height * 0.06)
            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.60, window_width * 0.20, window_height * 0.06)

        # Starter wählen
        elif menu_state == "choose_starter":
            title = font.render("Wähle einen Starter.", True, WHITE)
            # Starter wählen
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))
            pygame.draw.rect(screen, GREEN,(window_width * 0.225, window_height * 0.30, window_width * 0.15, window_height * 0.475))
            choose_bauz_button = draw_button("Bauz", window_width * 0.25, window_height * 0.70, window_width * 0.10, window_height * 0.06)
            screen.blit(front_bauz_img, (window_width * 0.25, window_height * 0.50))
            pygame.draw.rect(screen, RED,(window_width * 0.425, window_height * 0.30, window_width * 0.15, window_height * 0.475))
            choose_flamiau_button = draw_button("Flamiau", window_width * 0.45, window_height * 0.70, window_width * 0.10, window_height * 0.06)
            screen.blit(front_flamiau_img, (window_width * 0.45, window_height * 0.50))
            pygame.draw.rect(screen, BLUE,(window_width * 0.625, window_height * 0.30, window_width * 0.15, window_height * 0.475))
            choose_robball_button = draw_button("Robball", window_width * 0.65, window_height * 0.70, window_width * 0.10, window_height * 0.06)
            screen.blit(front_robball_img, (window_width * 0.65, window_height * 0.50))

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.80, window_width * 0.20, window_height * 0.06)

        # Hauptmenü
        elif menu_state == "main_menu":
            title = font.render("Hauptmenü", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            start_combat_button = draw_button("Kämpfen", window_width * 0.40, window_height * 0.40, window_width * 0.20, window_height * 0.06)
            view_pokemon_button = draw_button("Pokemon", window_width * 0.40, window_height * 0.50, window_width * 0.20, window_height * 0.06)
            altar_for_sacrifices_button = draw_button("Altar zum Opfern", window_width * 0.40, window_height * 0.60, window_width * 0.20, window_height * 0.06)
            save_button = draw_button("Speichern", window_width * 0.40, window_height * 0.70, window_width * 0.20, window_height * 0.06)
            quit_button = draw_button("Quit", window_width * 0.40, window_height * 0.80, window_width * 0.20, window_height * 0.05)
            if show_confirm_quit == True:
                draw_button("",  window_width * 0.35, window_height * 0.30, window_width * 0.30, window_height * 0.30)
                draw_text("Hast du gespeichert?", window_width * 0.50, window_height * 0.33, BLACK)
                confirm_quit_button = draw_button("Ja", window_width * 0.375, window_height * 0.36, window_width * 0.25, window_height * 0.04)
                cancel_quit_button = draw_button("Oh nein!!!", window_width * 0.375, window_height * 0.41, window_width * 0.25, window_height * 0.14)

        # Kampf annehmen
        elif menu_state == "start_combat":
            title = font.render("Kämpfen", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))
            challenge_text = draw_text(str(enemy_text), window_width * 0.50, window_height * 0.50)
            accept_button = draw_button("Lass uns kämpfen!", window_width * 0.40, window_height * 0.60, window_width * 0.20, window_height * 0.06)
            back_button = draw_button("Ne kein Bock", window_width * 0.40, window_height * 0.70, window_width * 0.20, window_height * 0.06)

        # Kampf Aktion wählen
        elif menu_state == "combat_menu":
            load_back_img(battle.spieler_active_poke)
            load_front_img(battle.enemy_active_poke)

            fight_button = draw_button("Angreifen", window_width * 0.50, window_height * 0.80, window_width * 0.25, window_height * 0.20)
            swap_pokemon_button = draw_button("Pokemon", window_width * 0.75, window_height * 0.80, window_width * 0.25, window_height * 0.20)

            what_do_you_do_text = draw_button("Was willst du machen?", window_width * 0.00, window_height * 0.80, window_width * 0.50, window_height * 0.20)
            # Textfeld von Spieler Pokemon
            ally_pokemon_text_field = draw_button("", window_width * 0.70, window_height * 0.60, window_width * 0.30, window_height * 0.15)
            pokemon_name_ally_text = draw_text(getattr(battle.spieler_active_poke, "name", None), window_width * 0.85, window_height * 0.625, BLACK)
            pokemon_level_ally_text = draw_text("Level:" + str(getattr(battle.spieler_active_poke, "level", None)), window_width * 0.75, window_height * 0.700, BLACK)
            pokemon_hp_ally_text = draw_text(f"HP:{round(getattr(battle.spieler_active_poke, "currentkp", None), 2)}", window_width * 0.90, window_height * 0.675, RED)
            pokemon_ep_ally_text = draw_text(f"EP:{round(getattr(battle.spieler_active_poke, "ep", None), 2)}", window_width * 0.90, window_height * 0.725, BLUE)
            # Textfeld von Gegner Pokemon
            enemy_pokemon_text_field = draw_button("", window_width * 0.00, window_height * 0.05, window_width * 0.30, window_height * 0.15)
            pokemon_name_enemy_text = draw_text(getattr(battle.enemy_active_poke, "name", None), window_width * 0.15, window_height * 0.075, BLACK)
            pokemon_level_enemy_text = draw_text("Level:" + str(getattr(battle.enemy_active_poke, "level", None)), window_width * 0.05, window_height * 0.150, BLACK)
            pokemon_hp_enemy_text = draw_text(f"HP:{round(getattr(battle.enemy_active_poke, "currentkp", None), 2)}", window_width * 0.20, window_height * 0.125, RED)
            pokemon_ep_enemy_text = draw_text("EP:" + str(getattr(battle.enemy_active_poke, "ep", None)), window_width * 0.20, window_height * 0.175, BLUE)

        # Kampf Attacke wählen
        elif menu_state == "choose_attack":
            load_back_img(battle.spieler_active_poke)
            load_front_img(battle.enemy_active_poke)

            attack1_button = draw_button("Physiche-Attacke", window_width * 0.50, window_height * 0.80, window_width * 0.25, window_height * 0.20)
            attack2_button = draw_button("Spezial-Attacke", window_width * 0.75, window_height * 0.80, window_width * 0.25, window_height * 0.20)
            changed_my_mind_button = draw_button("Zurück", window_width * 0.40, window_height * 0.80, window_width * 0.10, window_height * 0.20)

            what_do_you_do_text = draw_button("Welche Attacke?", window_width * 0.00, window_height * 0.80, window_width * 0.40, window_height * 0.20)
            # Textfeld von Spieler Pokemon
            ally_pokemon_text_field = draw_button("", window_width * 0.70, window_height * 0.60, window_width * 0.30, window_height * 0.15)
            pokemon_name_ally_text = draw_text(getattr(battle.spieler_active_poke, "name", None), window_width * 0.85, window_height * 0.625, BLACK)
            pokemon_level_ally_text = draw_text("Level:" + str(getattr(battle.spieler_active_poke, "level", None)), window_width * 0.75, window_height * 0.700, BLACK)
            pokemon_hp_ally_text = draw_text(f"HP:{round(getattr(battle.spieler_active_poke, "currentkp", None), 2)}", window_width * 0.90, window_height * 0.675, RED)
            pokemon_ep_ally_text = draw_text(f"EP:{round(getattr(battle.spieler_active_poke, "ep", None), 2)}", window_width * 0.90, window_height * 0.725, BLUE)
            # Textfeld von Gegner Pokemon
            enemy_pokemon_text_field = draw_button("", window_width * 0.00, window_height * 0.05, window_width * 0.30, window_height * 0.15)
            pokemon_name_enemy_text = draw_text(getattr(battle.enemy_active_poke, "name", None), window_width * 0.15, window_height * 0.075, BLACK)
            pokemon_level_enemy_text = draw_text("Level:" + str(getattr(battle.enemy_active_poke, "level", None)), window_width * 0.05, window_height * 0.150, BLACK)
            pokemon_hp_enemy_text = draw_text(f"HP:{round(getattr(battle.enemy_active_poke, "currentkp", None), 2)}", window_width * 0.20, window_height * 0.125, RED)
            pokemon_ep_enemy_text = draw_text("EP:" + str(getattr(battle.enemy_active_poke, "ep", None)), window_width * 0.20, window_height * 0.175, BLUE)

        # Kampf Pokemon wechseln
        elif menu_state == "swap_pokemon":
            load_back_img(battle.spieler_active_poke)
            load_front_img(battle.enemy_active_poke)

            # Textfeld von Spieler Pokemon
            ally_pokemon_text_field = draw_button("", window_width * 0.70, window_height * 0.60, window_width * 0.30, window_height * 0.15)
            pokemon_name_ally_text = draw_text(getattr(battle.spieler_active_poke, "name", None), window_width * 0.85, window_height * 0.625, BLACK)
            pokemon_level_ally_text = draw_text("Level:" + str(getattr(battle.spieler_active_poke, "level", None)), window_width * 0.75, window_height * 0.700, BLACK)
            pokemon_hp_ally_text = draw_text(f"HP:{round(getattr(battle.spieler_active_poke, "currentkp", None), 2)}", window_width * 0.90, window_height * 0.675, RED)
            pokemon_ep_ally_text = draw_text(f"EP:{round(getattr(battle.spieler_active_poke, "ep", None), 2)}", window_width * 0.90, window_height * 0.725, BLUE)
            # Textfeld von Gegner Pokemon
            enemy_pokemon_text_field = draw_button("", window_width * 0.00, window_height * 0.05, window_width * 0.30, window_height * 0.15)
            pokemon_name_enemy_text = draw_text(getattr(battle.enemy_active_poke, "name", None), window_width * 0.15, window_height * 0.075, BLACK)
            pokemon_level_enemy_text = draw_text("Level:" + str(getattr(battle.enemy_active_poke, "level", None)), window_width * 0.05, window_height * 0.150, BLACK)
            pokemon_hp_enemy_text = draw_text(f"HP:{round(getattr(battle.enemy_active_poke, "currentkp", None), 2)}", window_width * 0.20, window_height * 0.125, RED)
            pokemon_ep_enemy_text = draw_text("EP:" + str(getattr(battle.enemy_active_poke, "ep", None)), window_width * 0.20, window_height * 0.175, BLUE)

            if len(battle.spieler_poke_team) > 1:
                pokemon1_button = draw_button(battle.spieler_poke_team[1].name, window_width * 0.50, window_height * 0.80, window_width * 0.25, window_height * 0.20)
            if len(battle.spieler_poke_team) > 2:
                pokemon2_button = draw_button(battle.spieler_poke_team[2].name, window_width * 0.75, window_height * 0.80, window_width * 0.25, window_height * 0.20)
            if len(battle.spieler_poke_team) > 3:
                pokemon3_button = draw_button(battle.spieler_poke_team[3].name, window_width * 0.50, window_height * 0.60, window_width * 0.25, window_height * 0.20)
            if len(battle.spieler_poke_team) > 4:
                pokemon4_button = draw_button(battle.spieler_poke_team[4].name, window_width * 0.75, window_height * 0.60, window_width * 0.25, window_height * 0.20)
            if len(battle.spieler_poke_team) > 5:
                pokemon5_button = draw_button(battle.spieler_poke_team[5].name, window_width * 0.75, window_height * 0.40, window_width * 0.25, window_height * 0.20)

            changed_my_mind_button = draw_button("Zurück", window_width * 0.40, window_height * 0.80, window_width * 0.10, window_height * 0.20)

            what_do_you_do_text = draw_button("Welches Pokemon?", window_width * 0.00, window_height * 0.80, window_width * 0.40, window_height * 0.20)

        # Kampfübersicht
        elif menu_state == "fight_overview":
            title = font.render("Kampfübersicht", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            pokemon_view_text_field = draw_button("", window_width * 0.30, window_height * 0.29, window_width * 0.40, window_height * 0.50)

            height_adder = 0.45

            for logs in battle.eplog:
                ep_text = ""
                ep_text += logs[0]+": "
                ep_text += "+"+str(logs[1])+" EP"
                ep_text_pos_y = window_height * height_adder
                ep_log_text_field = draw_text(ep_text, window_width * 0.50, ep_text_pos_y, BLACK)
                height_adder += 0.05

            if log == "game_over_player":
                text1 = "Du hast verloren"
            elif log == "game_over_enemy":
                text1 = "Du hast gewonnen"

            draw_text(text1, window_width * 0.50, window_height * 0.35, BLACK)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.70, window_width * 0.20, window_height * 0.06)

        # Pokemon
        elif menu_state == "view_pokemon":
            title = font.render("Pokemon", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            pokemonliste = [str(poke.name) for poke in view_pokemon_scrollbar.get_scrollbarliste()]

            view_pokemon_stats_button_list = []

            width_adder = 0.10
            height_adder = 0.30
            line_count = 0
            for poke in pokemonliste:
                if line_count == 4:
                    line_count = 0
                    height_adder += 0.10
                    width_adder = 0.10
                btn = draw_button(poke, window_width * width_adder, window_height * height_adder, window_width * 0.18, window_height * 0.06)
                view_pokemon_stats_button_list.append((poke, btn))
                width_adder += 0.20
                line_count += 1
            
            if view_pokemon_scrollbar.check_scrollable():
                view_pokemon_scrollbar.draw_scrollbar_indicator_frame()
                view_pokemon_scrollbar.draw_scrollbar_indicator()
            
            team_editor_button = draw_button("Team-Editor", window_width * 0.40, window_height * 0.78, window_width * 0.20, window_height * 0.06)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20, window_height * 0.06)

        # Team Editor
        elif menu_state == "team_editor":
            title = font.render("Team-Editor", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            pokemonliste = [str(poke.name) for poke in team_editor_scrollbar.get_scrollbarliste()]

            view_pokemon_stats_button_list = []

            width_adder = 0.10
            height_adder = 0.30
            line_count = 0
            for poke in pokemonliste:
                if line_count == 4:
                    line_count = 0
                    height_adder += 0.10
                    width_adder = 0.10
                btn = draw_button(poke, window_width * width_adder, window_height * height_adder, window_width * 0.18, window_height * 0.06)
                view_pokemon_stats_button_list.append((poke, btn))
                width_adder += 0.20
                line_count += 1
            
            first_slot.text = ""
            second_slot.text = ""
            third_slot.text = ""
            fourth_slot.text = ""
            fifth_slot.text = ""
            sixth_slot.text = ""

            for i in range(len(spieler.pokemon_team)):
                if i == 0:
                    first_slot.text = spieler.pokemon_team[0].name
                if i == 1:
                    second_slot.text = spieler.pokemon_team[1].name
                if i == 2:
                    third_slot.text = spieler.pokemon_team[2].name
                if i == 3:
                    fourth_slot.text = spieler.pokemon_team[3].name
                if i == 4:
                    fifth_slot.text = spieler.pokemon_team[4].name
                if i == 5:
                    sixth_slot.text = spieler.pokemon_team[5].name

            first_slot.draw()
            second_slot.draw()
            third_slot.draw()
            fourth_slot.draw()
            fifth_slot.draw()
            sixth_slot.draw()

            if team_editor_scrollbar.check_scrollable():
                team_editor_scrollbar.draw_scrollbar_indicator_frame()
                team_editor_scrollbar.draw_scrollbar_indicator()

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20, window_height * 0.06)

        # Pokemon Stats
        elif menu_state == "pokemon_stats":
            if selected_pokemon:
                title = font.render(f"{selected_pokemon.name}", True, WHITE)
            else:
                title = font.render("Pokemon Stats", True, WHITE)

            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            pokemon_view_text_field = draw_button("", window_width * 0.30, window_height * 0.29, window_width * 0.40, window_height * 0.55)

            # Echte Werte anzeigen
            draw_text(f"Level: {selected_pokemon.level}", window_width * 0.43, window_height * 0.32, BLACK)
            draw_text(f"EP: {round(selected_pokemon.ep, 2)}/{round(100 * selected_pokemon.level ** 1.1, 2)}", window_width * 0.43, window_height * 0.37, BLACK)
            draw_text(f"Typ: {', '.join(selected_pokemon.typ)}", window_width * 0.43, window_height * 0.42, BLACK)
            draw_text(f"KP: {selected_pokemon.maxkp}", window_width * 0.43, window_height * 0.47, BLACK)
            draw_text(f"ATK: {selected_pokemon.atk}", window_width * 0.43, window_height * 0.52, BLACK)
            draw_text(f"DEF: {selected_pokemon.defence}", window_width * 0.43, window_height * 0.57, BLACK)
            draw_text(f"SPATK: {selected_pokemon.spatk}", window_width * 0.43, window_height * 0.62, BLACK)
            draw_text(f"SPDEF: {selected_pokemon.spdef}", window_width * 0.43, window_height * 0.67, BLACK)
            draw_text(f"Initiative: {selected_pokemon.init}", window_width * 0.43, window_height * 0.72, BLACK)

            # FP anzeigen
            draw_text(f"FP: {selected_pokemon.fp}", window_width * 0.65, window_height * 0.42, BLACK)

            # FFP anzeigen
            draw_text(f"FFP: {altar.fp_amount}", window_width * 0.65, window_height * 0.38, BLACK)
            add_fp_to_pokemon_button = draw_button("Convert", window_width * 0.55, window_height * 0.363, window_width * 0.06, window_height * 0.03)

            # Buttons zum verteilen der freien Statuswertpunkte
            pokemon_view_kp_plus_button = draw_button("+", window_width * 0.63, window_height * 0.46, window_width * 0.02, window_height * 0.03)
            pokemon_view_kp_minus_button = draw_button("-", window_width * 0.66, window_height * 0.46, window_width * 0.02, window_height * 0.03)
            pokemon_view_atk_plus_button = draw_button("+", window_width * 0.63, window_height * 0.51, window_width * 0.02, window_height * 0.03)
            pokemon_view_atk_minus_button = draw_button("-", window_width * 0.66, window_height * 0.51, window_width * 0.02, window_height * 0.03)
            pokemon_view_def_plus_button = draw_button("+", window_width * 0.63, window_height * 0.56, window_width * 0.02, window_height * 0.03)
            pokemon_view_def_minus_button = draw_button("-", window_width * 0.66, window_height * 0.56, window_width * 0.02, window_height * 0.03)
            pokemon_view_spatk_plus_button = draw_button("+", window_width * 0.63, window_height * 0.61, window_width * 0.02, window_height * 0.03)
            pokemon_view_spatk_minus_button = draw_button("-", window_width * 0.66, window_height * 0.61, window_width * 0.02, window_height * 0.03)
            pokemon_view_spdef_plus_button = draw_button("+", window_width * 0.63, window_height * 0.66, window_width * 0.02, window_height * 0.03)
            pokemon_view_spdef_minus_button = draw_button("-", window_width * 0.66, window_height * 0.66, window_width * 0.02, window_height * 0.03)
            pokemon_view_init_plus_button = draw_button("+", window_width * 0.63, window_height * 0.71, window_width * 0.02, window_height * 0.03)
            pokemon_view_init_minus_button = draw_button("-", window_width * 0.66, window_height * 0.71, window_width * 0.02, window_height * 0.03)

            physical_attack_button = draw_button(selected_pokemon.attacken[0].__class__.__name__, window_width * 0.32, window_height * 0.79, window_width * 0.16, window_height * 0.04)

            special_attack_button = draw_button(selected_pokemon.attacken[1].__class__.__name__,  window_width * 0.52, window_height * 0.79, window_width * 0.16, window_height * 0.04)

            if selected_pokemon in spieler.pokemon_team:
                plusorminus = "-"
            elif selected_pokemon not in spieler.pokemon_team:
                plusorminus = "+"
            add_pokemon_to_team_button = draw_button(f"{plusorminus} Team", window_width * 0.32, window_height * 0.74, window_width * 0.16, window_height * 0.04)

            if evolution.check_evolution(selected_pokemon) != None:
                evolution_button = draw_button("Entwickeln", window_width * 0.52, window_height * 0.74, window_width * 0.16, window_height * 0.04)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20, window_height * 0.06)

        # Physische Attacke ansehen/wechseln
        elif menu_state == "view_physical_attack":
            title = font.render(selected_pokemon.attacken[0].__class__.__name__, True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            attack_view_text_field = draw_button("", window_width * 0.33, window_height * 0.29, window_width * 0.34, window_height * 0.45)

            draw_text(f"Schaden: {selected_pokemon.attacken[0].atkdmg}", window_width * 0.50, window_height * 0.37, BLACK)
            draw_text(f"Typ: {selected_pokemon.attacken[0].typ}", window_width * 0.50, window_height * 0.42, BLACK)
            draw_text(f"Attackentyp: {selected_pokemon.attacken[0].dmgtype}", window_width * 0.50, window_height * 0.47, BLACK)

            draw_text(f"Kosten: {altar.change_attack_cost} Besiegte Trainer", window_width * 0.50, window_height * 0.60, BLACK)
            choose_attack_button = draw_button("Wechseln", window_width * 0.42, window_height * 0.65, window_width * 0.16, window_height * 0.04)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.75, window_width * 0.20, window_height * 0.06)

        # Neue Physische Attacke auswählen
        elif menu_state == "choose_new_physical_attack":
            title = font.render("Neue Attacke wählen", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            alle_attacken = [cls() for cls in Attacken]

            gefilterte_attacken = []
            for attacke in alle_attacken:
                if (getattr(attacke, "dmgtype") == "physisch"
                and getattr(attacke, "typ") in selected_pokemon.typ
                and attacke.__class__.__name__ != selected_pokemon.attacken[0].__class__.__name__):
                    gefilterte_attacken.append(attacke)

            attackenliste = [attacke for attacke in gefilterte_attacken]

            view_attacken_button_list = []

            width_adder = 0.10
            height_adder = 0.30
            line_count = 0
            for attacke in attackenliste:
                if line_count == 4:
                    line_count = 0
                    height_adder += 0.08
                    width_adder = 0.10
                btn = draw_button(
                    attacke.__class__.__name__,
                    window_width * width_adder,
                    window_height * height_adder,
                    window_width * 0.18,
                    window_height * 0.06
                )
                view_attacken_button_list.append((attacke, btn))
                width_adder += 0.20
                line_count += 1

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20,  window_height * 0.06)

        # Spezial Attacke ansehen/wechseln
        elif menu_state == "view_special_attack":
            title = font.render(selected_pokemon.attacken[1].__class__.__name__, True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            attack_view_text_field = draw_button("", window_width * 0.33, window_height * 0.29, window_width * 0.34, window_height * 0.45)

            draw_text(f"Schaden: {selected_pokemon.attacken[1].atkdmg}", window_width * 0.50, window_height * 0.37, BLACK)
            draw_text(f"Typ: {selected_pokemon.attacken[1].typ}", window_width * 0.50, window_height * 0.42, BLACK)
            draw_text(f"Attackentyp: {selected_pokemon.attacken[1].dmgtype}", window_width * 0.50, window_height * 0.47, BLACK)

            draw_text(f"Kosten: {altar.change_attack_cost} Besiegte Trainer", window_width * 0.50, window_height * 0.60, BLACK)
            choose_attack_button = draw_button("Wechseln", window_width * 0.42, window_height * 0.65, window_width * 0.16, window_height * 0.04)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20, window_height * 0.06)

        # Neue Spezial Attacke auswählen
        elif menu_state == "choose_new_special_attack":
            title = font.render("Neue Attacke wählen", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            alle_attacken = [cls() for cls in Attacken]

            gefilterte_attacken = []
            for attacke in alle_attacken:
                if (getattr(attacke, "dmgtype") == "spezial"
                        and getattr(attacke, "typ") in selected_pokemon.typ
                        and attacke.__class__.__name__ != selected_pokemon.attacken[1].__class__.__name__):
                    gefilterte_attacken.append(attacke)

            attackenliste = [attacke for attacke in gefilterte_attacken]

            view_attacken_button_list = []

            width_adder = 0.10
            height_adder = 0.30
            line_count = 0
            for attacke in attackenliste:
                if line_count == 4:
                    line_count = 0
                    height_adder += 0.08
                    width_adder = 0.10
                btn = draw_button(
                    attacke.__class__.__name__,
                    window_width * width_adder,
                    window_height * height_adder,
                    window_width * 0.18,
                    window_height * 0.06
                )
                view_attacken_button_list.append((attacke, btn))
                width_adder += 0.20
                line_count += 1

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.85, window_width * 0.20, window_height * 0.06)

        # Altar zum Opfern
        elif menu_state == "altar_for_sacrifices":
            title = font.render("Altar zum Opfern", True, WHITE)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, window_height * 0.2))

            available_bodys_text_field = draw_button("", window_width * 0.35, window_height * 0.40, window_width * 0.30, window_height * 0.15)

            available_trainer_bodys_text = draw_text(f"Besiegte Trainer:{altar.trainer_bodies}", window_width * 0.50, window_height * 0.45, BLACK)
            available_pokemon_bodys_text = draw_text(f"Besiegte Pokemon:{altar.pokemon_bodies}", window_width * 0.50, window_height * 0.50, BLACK)

            sacrifice_for_pokemon_button = draw_button("Opfern für Pokemon", window_width * 0.40, window_height * 0.57, window_width * 0.20, window_height * 0.06)
            sacrifice_for_fp_button = draw_button("Opfern für FFP", window_width * 0.40, window_height * 0.65, window_width * 0.20, window_height * 0.06)

            back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.73, window_width * 0.20, window_height * 0.06)


        pygame.display.flip()

    pygame.quit()
    sys.exit()
