import random
print("You encountered a merchant!")

class Merchant():
    def __init__(info, ask_trade, trader_ans, xp):
        info.ask_trade = ask_trade
        info.trader_ans = trader_ans
        info.xp = xp

    def trade(info, ask_trade, trader_ans):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                trader_ans == 'Yes'
                xp += 20
                print('The trader accepts the offer!')
            else:
                trader_ans == 'No'
                print('Trader declined :(')
                break

class Hero:
    def __init__(self, name, level, attack_power, health, xp):
        self.name = name
        self.xp = xp
        self.level = level
        self.attack_power = attack_power
        self.health = health

    def level_up(level, health, attack_power, xp):
        if xp == {200, 400, 800, 1000}:
            level = level + 1
            health += 50
            attack_power += 50

    def attack_monster(self, monster):
        monster.health -= self.attack_power
        print(f"{self.name} attacks {monster.name} for {self.attack_power} damage!")

    def win(self, monster):
        if monster.health <= 0:
            level = level + 1
            print("You won the challenge!")

    def lose(self):
        if self.health <= 0:
            print("Game Over")
        
class Monster():
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.damage = 0

    def generate_monster():
        

    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")

    def take_damage(self,player,player_attack):
        self.health -= player_attack
        print(f"{player.name} attacks {self.name} for {player_attack} damage!")



# #in encounter code
# provoke = input("challenge monster to a battle? Y/N: ").upper()
# if provoke == 'Y':
# 	monster.attack
# else:
# 	print("challenge forfeited")
# ####