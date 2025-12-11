import random
import Effektivitaet

class Battle:
    def __init__(self, spieler_active_poke, spieler_poke_team, spieler_selected_move, enemy_active_poke, enemy_poke_team, altar):
        self.spieler_active_poke = spieler_active_poke
        self.spieler_poke_team = spieler_poke_team
        self.spieler_selected_move = spieler_selected_move
        self.enemy_active_poke = enemy_active_poke
        self.enemy_poke_team = enemy_poke_team
        self.enemy_move = None
        self.altar = altar
        self.player_dead_pokemon = []

    def __calc_damage_physic(self, attacker, defender) -> float:
        return round((attacker.level * 0.4 + 2)
                      * attacker.atk
                      * attacker.attacken[0].atkdmg
                      / (10 * defender.defence)
                      * Effektivitaet.get_effectiveness(attacker.attacken[0].typ, defender.typ[0]), 2)

    def __calc_damage_special(self, attacker, defender) -> float:
        return round((attacker.level * 0.4 + 2)
                      * attacker.spatk
                      * attacker.attacken[0].atkdmg
                      / (10 * defender.spdef)
                      * Effektivitaet.get_effectiveness(attacker.attacken[1].typ, defender.typ[0]), 2)

    def __active_fainted(self, active_pokemon) -> bool:
        if active_pokemon.currentkp < 0:
            active_pokemon.currentkp = 0
            return True
        return False

    def __team_dead(self, team) -> bool:
        if len(team) <= 0:
            return True
        return False

    def __process_fainted(self, active_pokemon) -> None:
        self.player_dead_pokemon.append(active_pokemon)
        self.spieler_poke_team.remove(active_pokemon)

    def __process_player_win(self) -> None:
        self.spieler_active_poke.ep += 100
        self.spieler_active_poke.check_level_up()
        self.altar.pokemon_bodies += 1

    def player_attack_physic(self):
        spieler_active_poke_init = getattr(self.spieler_active_poke, "init")
        enemy_active_poke_init = getattr(self.enemy_active_poke, "init")

        if spieler_active_poke_init > enemy_active_poke_init:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            # Schaden der Spielerattacke wird berechnet
            self.enemy_active_poke.currentkp -= self.__calc_damage_physic(self.spieler_active_poke,
                                                                          self.enemy_active_poke)
            if self.enemy_active_poke.currentkp > 0:
                # Gegner hat überlebt -> physiche Attacke
                if self.enemy_move == "attack_physic":
                    self.spieler_active_poke.currentkp -= self.__calc_damage_physic(self.enemy_active_poke,
                                                                                    self.spieler_active_poke)
                    if self.__active_fainted(self.spieler_active_poke):
                        # Spieler Pokemon austauschen bzw Game Over
                        self.__process_fainted(self.spieler_active_poke)
                        if not self.__team_dead(self.spieler_poke_team):
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
                # Gegner hat überlebt -> spezial-Attacke
                elif self.enemy_move == "attack_special":
                    self.spieler_active_poke.currentkp -= self.__calc_damage_special(self.enemy_active_poke,
                                                                                     self.spieler_active_poke)
                    if self.__active_fainted(self.spieler_active_poke):
                        # Spieler Pokemon austauschen bzw Game Over
                        self.__process_fainted(self.spieler_active_poke)
                        if not self.__team_dead(self.spieler_poke_team):
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
            else:
                # EP an aktives Spieler Pokemon geben
                self.__process_player_win()
                # Gegner Pokemon austauschen bzw Game Over
                self.enemy_poke_team.remove(self.enemy_active_poke)
                if not self.__team_dead(self.enemy_poke_team):
                    self.enemy_active_poke = self.enemy_poke_team[0]
                else:
                    return "game_over_enemy"
        else:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            if self.enemy_move == "attack_physic":
                self.spieler_active_poke.currentkp -= self.__calc_damage_physic(self.enemy_active_poke,
                                                                                self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    self.enemy_active_poke.currentkp -= self.__calc_damage_physic(self.spieler_active_poke,
                                                                                  self.enemy_active_poke)
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.__process_player_win()
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if not self.__team_dead(self.enemy_poke_team):
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.__calc_damage_special(self.enemy_active_poke,
                                                                                 self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    self.enemy_active_poke.currentkp -= self.__calc_damage_physic(self.spieler_active_poke,
                                                                                   self.enemy_active_poke)
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.__process_player_win()
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if not self.__team_dead(self.enemy_poke_team):
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"



    def player_attack_special(self):
        spieler_active_poke_init = getattr(self.spieler_active_poke, "init")
        enemy_active_poke_init = getattr(self.enemy_active_poke, "init")

        if spieler_active_poke_init > enemy_active_poke_init:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            # Schaden der Spielerattacke wird berechnet
            self.enemy_active_poke.currentkp -= self.__calc_damage_special(self.spieler_active_poke,
                                                                           self.enemy_active_poke)
            if self.enemy_active_poke.currentkp > 0:
                # Gegner hat überlebt -> physiche Attacke
                if self.enemy_move == "attack_physic":
                    self.spieler_active_poke.currentkp -= self.__calc_damage_physic(self.enemy_active_poke,
                                                                                    self.spieler_active_poke)
                    if self.__active_fainted(self.spieler_active_poke):
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if not self.__team_dead(self.spieler_poke_team):
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
                # Gegner hat überlebt -> spezial-Attacke
                elif self.enemy_move == "attack_special":
                    self.spieler_active_poke.currentkp -= self.__calc_damage_special(self.enemy_active_poke,
                                                                                     self.spieler_active_poke)
                    if self.__active_fainted(self.spieler_active_poke):
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if not self.__team_dead(self.spieler_poke_team):
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
            else:
                # EP an aktives Spieler Pokemon geben
                self.__process_player_win()
                # Gegner Pokemon austauschen bzw Game Over
                self.enemy_poke_team.remove(self.enemy_active_poke)
                if not self.__team_dead(self.enemy_poke_team):
                    self.enemy_active_poke = self.enemy_poke_team[0]
                else:
                    return "game_over_enemy"
        else:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            if self.enemy_move == "attack_physic":
                self.spieler_active_poke.currentkp -= self.__calc_damage_physic(self.enemy_active_poke,
                                                                                self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    self.enemy_active_poke.currentkp -= self.__calc_damage_special(self.spieler_active_poke,
                                                                                   self.enemy_active_poke)
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben und Levelup checken
                        self.__process_player_win()
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if not self.__team_dead(self.enemy_poke_team):
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.__calc_damage_special(self.enemy_active_poke,
                                                                                 self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    self.enemy_active_poke.currentkp -= self.__calc_damage_special(self.spieler_active_poke,
                                                                                   self.enemy_active_poke)
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.__process_player_win()
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if not self.__team_dead(self.enemy_poke_team):
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"


    def swap_pokemon_in_battle(self, slot):
        if self.spieler_poke_team[slot].currentkp > 0:
            self.spieler_active_poke = self.spieler_poke_team[slot]
            self.spieler_poke_team[slot] = self.spieler_poke_team[0]
            self.spieler_poke_team[0] = self.spieler_active_poke
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            if self.enemy_move == "attack_physic":
                self.spieler_active_poke.currentkp -= self.__calc_damage_physic(self.enemy_active_poke,
                                                                                self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.__calc_damage_special(self.enemy_active_poke,
                                                                                 self.spieler_active_poke)
                if self.__active_fainted(self.spieler_active_poke):
                    # Spieler Pokemon austauschen bzw Game Over
                    self.__process_fainted(self.spieler_active_poke)
                    if not self.__team_dead(self.spieler_poke_team):
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"


    # Spieler Pokemon Team resetten
    def reset_player_team(self):
        # Alle Pokemon ins Spieler Team zurück
        dead_poke_count = len(self.player_dead_pokemon)
        for i in range(dead_poke_count):
            moved_pokemon = self.player_dead_pokemon[0]

            self.player_dead_pokemon.remove(moved_pokemon)
            self.spieler_poke_team.append(moved_pokemon)
        # Heilen
        heal_number = len(self.spieler_poke_team)
        count = 0
        for i in range(heal_number):
            healed_pokemon = self.spieler_poke_team[count]
            healed_pokemon.currentkp = healed_pokemon.maxkp
            count += 1
