from random import *



class Unit:
    def __init__(self, name, rarity, rank):
        self.name = name
        self.rarity = rarity
        self.rank = rank


unit_a_one = Unit('A1', 1, 1)
unit_a_two = Unit('A2', 1, 1)
unit_a_three = Unit('A3', 1, 1)
unit_a_four = Unit('A4', 1, 1)
unit_a_five = Unit('A5', 1, 1)
unit_b_one = Unit('B1', 2, 1)
unit_b_two = Unit('B2', 2, 1)
unit_b_three = Unit('B3', 2, 1)
unit_b_four = Unit('B4', 2, 1)
unit_b_five = Unit('B5', 2, 1)

available_one_cost_units = [unit_a_one.name, unit_a_two.name, unit_a_three.name, unit_a_four.name, unit_a_five.name]
available_two_cost_units = [unit_b_one.name, unit_b_two.name, unit_b_three.name, unit_b_four.name, unit_b_five.name]
available_three_cost_units = [unit_a_one.name, unit_a_two.name, unit_a_three.name, unit_a_four.name, unit_a_five.name]
available_four_cost_units = [unit_a_one.name, unit_a_two.name, unit_a_three.name, unit_a_four.name, unit_a_five.name]
available_five_cost_units = [unit_a_one.name, unit_a_two.name, unit_a_three.name, unit_a_four.name, unit_a_five.name]


class Shop:
    one_cost_chance = 1
    two_cost_chance = 0
    three_cost_chance = 0
    four_cost_chance = 0
    five_cost_chance = 0
    counter = 0
    turn_start_units = []

    def __init__(self, player):
        self.player = player

    def cost_adjust(self, one_cost, two_cost, three_cost, four_cost, five_cost):
        Shop.one_cost_chance = one_cost
        Shop.two_cost_chance = two_cost
        Shop.three_cost_chance = three_cost
        Shop.four_cost_chance = four_cost
        Shop.five_cost_chance = five_cost

    def turn_start_shop(self):

        while Shop.counter == 0:
            if random() < Shop.one_cost_chance and Shop.counter == 0:
                Shop.turn_start_units.append(available_one_cost_units[randint(0, 4)])
            Shop.counter += 1
        print(Shop.turn_start_units)

    def randomize_shop(self):
        unit_count = 0
        reroll_units = []
        while unit_count <= 4:
            if random() < Shop.one_cost_chance:
                reroll_units.append(available_one_cost_units[randint(0, 4)])
                unit_count += 1
        print(reroll_units)

    def buy_exp(self):
        if p1.money >= 4:
            p1.exp += 4
            p1.money -= 4

    def adjust_shop_chance(self):
        match p1.level:
            case 3:
                Shop.cost_adjust(p1, .75, .25, 0, 0, 0)
            case 4:
                Shop.cost_adjust(p1, .55, .30, .15, 0, 0)
            case 5:
                Shop.cost_adjust(p1, .45, .33, .20, .02, 0)
            case 6:
                Shop.cost_adjust(p1, .25, .40, .30, .05, 0)
            case 7:
                Shop.cost_adjust(p1, .19, .30, .35, .15, .01)
            case 8:
                Shop.cost_adjust(self, .16, .20, .35, .25, .04)
            case 9:
                Shop.cost_adjust(self, .09, .15, .30, .30, 16)


def adjust_required_exp():
    match p1.level:
        case 2:
            p1.lvl_up_xp_required = 2
        case 3:
            p1.lvl_up_xp_required = 6
        case 4:
            p1.lvl_up_xp_required = 10
        case 5:
            p1.lvl_up_xp_required = 20
        case 6:
            p1.lvl_up_xp_required = 36
        case 7:
            p1.lvl_up_xp_required = 56
        case 8:
            p1.lvl_up_xp_required = 80


class Player:
    def __init__(self):
        self.level = 1
        self.money = 50
        self.exp = 0
        self.lvl_up_xp_required = 2

    def level_up(self):
        if p1.exp >= p1.lvl_up_xp_required:
            p1.level += 1
            p1.exp = 0


p1 = Player()

def gameplay_loop(self):

    while True:
        Shop.turn_start_shop(Shop)
        print(f"You are level {p1.level}, {p1.exp}/{p1.lvl_up_xp_required}")
        print(f'You have ${p1.money}')
        Player.level_up(p1)
        adjust_required_exp()

        if input('> ') == 'level':
            Shop.buy_exp(p1)

        if input('> ' == 'reroll'):
            Shop.randomize_shop(Shop)
    Shop.counter = 0

if __name__ == '__main__':
    gameplay_loop(p1)







