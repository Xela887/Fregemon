import random

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

    def player_attack_physic(self):
        spieler_active_poke_init = getattr(self.spieler_active_poke, "init")
        enemy_active_poke_init = getattr(self.enemy_active_poke, "init")

        if spieler_active_poke_init > enemy_active_poke_init:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            # Schaden der Spielerattacke wird berechnet
            spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.atk * self.spieler_active_poke.attacken[0].atkdmg / (10 * self.enemy_active_poke.defence), 2)
            self.enemy_active_poke.currentkp -= spieler_dmg
            if self.enemy_active_poke.currentkp > 0:
                # Gegner hat überlebt -> physiche Attacke
                if self.enemy_move == "attack_physic":
                    self.spieler_active_poke.currentkp -= self.enemy_attack_physic()    # Gegnerattacke
                    if self.spieler_active_poke.currentkp <= 0:
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if len(self.spieler_poke_team) >= 1:
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
                # Gegner hat überlebt -> spezial-Attacke
                elif self.enemy_move == "attack_special":
                    self.spieler_active_poke.currentkp -= self.enemy_attack_special()   # Gegnerattacke
                    if self.spieler_active_poke.currentkp <= 0:
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if len(self.spieler_poke_team) >= 1:
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
            else:
                # EP an aktives Spieler Pokemon geben
                self.spieler_active_poke.ep += 100
                self.spieler_active_poke.check_level_up()
                self.altar.pokemon_bodies += 1
                # Gegner Pokemon austauschen bzw Game Over
                self.enemy_poke_team.remove(self.enemy_active_poke)
                if len(self.enemy_poke_team) >= 1:
                    self.enemy_active_poke = self.enemy_poke_team[0]
                else:
                    return "game_over_enemy"
        else:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            if self.enemy_move == "attack_physic":
                self.spieler_active_poke.currentkp -= self.enemy_attack_physic()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.atk * self.spieler_active_poke.attacken[0].atkdmg / (10 * self.enemy_active_poke.defence), 2)
                    self.enemy_active_poke.currentkp -= spieler_dmg
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.spieler_active_poke.ep += 100
                        self.spieler_active_poke.check_level_up()
                        self.altar.pokemon_bodies += 1
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if len(self.enemy_poke_team) >= 1:
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.enemy_attack_special()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.atk * self.spieler_active_poke.attacken[0].atkdmg / (10 * self.enemy_active_poke.defence), 2)
                    self.enemy_active_poke.currentkp -= spieler_dmg
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.spieler_active_poke.ep += 100
                        self.spieler_active_poke.check_level_up()
                        self.altar.pokemon_bodies += 1
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if len(self.enemy_poke_team) >= 1:
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
            spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.spatk * self.spieler_active_poke.attacken[1].atkdmg / (10 * self.enemy_active_poke.spdef), 2)
            self.enemy_active_poke.currentkp -= spieler_dmg
            if self.enemy_active_poke.currentkp > 0:
                # Gegner hat überlebt -> physiche Attacke
                if self.enemy_move == "attack_physic":
                    self.spieler_active_poke.currentkp -= self.enemy_attack_physic()    # Gegnerattacke
                    if self.spieler_active_poke.currentkp <= 0:
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if len(self.spieler_poke_team) >= 1:
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
                # Gegner hat überlebt -> spezial-Attacke
                elif self.enemy_move == "attack_special":
                    self.spieler_active_poke.currentkp -= self.enemy_attack_special()   # Gegnerattacke
                    if self.spieler_active_poke.currentkp <= 0:
                        # Spieler Pokemon austauschen bzw Game Over
                        moved_pokemon = self.spieler_active_poke
                        self.spieler_poke_team.remove(moved_pokemon)
                        self.player_dead_pokemon.append(moved_pokemon)
                        if len(self.spieler_poke_team) >= 1:
                            self.spieler_active_poke = self.spieler_poke_team[0]
                        else:
                            return "game_over_player"
            else:
                # EP an aktives Spieler Pokemon geben
                self.spieler_active_poke.ep += 100
                self.spieler_active_poke.check_level_up()
                self.altar.pokemon_bodies += 1
                # Gegner Pokemon austauschen bzw Game Over
                self.enemy_poke_team.remove(self.enemy_active_poke)
                if len(self.enemy_poke_team) >= 1:
                    self.enemy_active_poke = self.enemy_poke_team[0]
                else:
                    return "game_over_enemy"
        else:
            # wählt den Move des Gegners
            enemy_moves = ["attack_physic", "attack_special"]
            self.enemy_move = random.choice(enemy_moves)
            if self.enemy_move == "attack_physic":
                self.spieler_active_poke.currentkp -= self.enemy_attack_physic()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.spatk * self.spieler_active_poke.attacken[1].atkdmg / (10 * self.enemy_active_poke.spdef), 2)
                    self.enemy_active_poke.currentkp -= spieler_dmg
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben und Levelup checken
                        self.spieler_active_poke.ep += 100
                        self.spieler_active_poke.check_level_up()
                        self.altar.pokemon_bodies += 1
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if len(self.enemy_poke_team) >= 1:
                            self.enemy_active_poke = self.enemy_poke_team[0]
                        else:
                            return "game_over_enemy"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.enemy_attack_special()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
                else:
                    # Schaden der Spielerattacke wird berechnet
                    spieler_dmg = round((self.spieler_active_poke.level * 0.4 + 2) * self.spieler_active_poke.spatk * self.spieler_active_poke.attacken[1].atkdmg / (10 * self.enemy_active_poke.spdef), 2)
                    self.enemy_active_poke.currentkp -= spieler_dmg
                    if self.enemy_active_poke.currentkp < 0:
                        # EP an aktives Spieler Pokemon geben
                        self.spieler_active_poke.ep += 100
                        self.spieler_active_poke.check_level_up()
                        self.altar.pokemon_bodies += 1
                        # Gegner Pokemon austauschen bzw Game Over
                        self.enemy_poke_team.remove(self.enemy_active_poke)
                        if len(self.enemy_poke_team) >= 1:
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
                self.spieler_active_poke.currentkp -= self.enemy_attack_physic()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
                        self.spieler_active_poke = self.spieler_poke_team[0]
                    else:
                        return "game_over_player"
            elif self.enemy_move == "attack_special":
                self.spieler_active_poke.currentkp -= self.enemy_attack_special()  # Gegnerattacke
                if self.spieler_active_poke.currentkp <= 0:
                    # Spieler Pokemon austauschen bzw Game Over
                    moved_pokemon = self.spieler_active_poke
                    self.spieler_poke_team.remove(moved_pokemon)
                    self.player_dead_pokemon.append(moved_pokemon)
                    if len(self.spieler_poke_team) >= 1:
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

    def enemy_attack_physic(self):
        enemy_dmg = round((self.enemy_active_poke.level * 0.4 + 2) * self.enemy_active_poke.atk * self.enemy_active_poke.attacken[0].atkdmg / (10 * self.spieler_active_poke.defence), 2)
        return enemy_dmg

    def enemy_attack_special(self):
        enemy_dmg = round((self.enemy_active_poke.level * 0.4 + 2) * self.enemy_active_poke.spatk * self.enemy_active_poke.attacken[1].atkdmg / (10 * self.spieler_active_poke.spdef), 2)
        return enemy_dmg
