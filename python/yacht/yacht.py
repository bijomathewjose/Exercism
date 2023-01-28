# Score categories.
# Change the values as you see fit.
YACHT = (lambda dice:50 if len(set(dice))==1 else 0)
ONES = (lambda dice:sum_of_digit(dice,1))
TWOS = (lambda dice:sum_of_digit(dice,2))
THREES = (lambda dice:sum_of_digit(dice,3))
FOURS = (lambda dice:sum_of_digit(dice,4))
FIVES = (lambda dice:sum_of_digit(dice,5))
SIXES = (lambda dice:sum_of_digit(dice,6))
FULL_HOUSE = (lambda dice:full_house(dice))
FOUR_OF_A_KIND =( lambda dice:four_kind(dice))

LITTLE_STRAIGHT =( lambda dice:30 if dice==[1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda dice:30 if dice==[2,3,4,5,6] else 0)
CHOICE = (lambda dice:sum(dice))


def score(dice, category):
    dice.sort()
    return category(dice)

def sum_of_digit(dice,digit):
    return digit*dice.count(digit)

def full_house(dice):
    if len(set(dice))==2:
        return sum(dice) if dice.count(dice[0]) in [2,3] else 0
    return 0
def four_kind(dice):
    four=[x for x in dice if dice.count(x)>=4]
    return 0 if len(four)==0 else four[0]*4
