from random import randint
class Robot:
    EXISTING=['']
    def __init__(self):
        self.generate_random_name()
        pass
    def generate_random_name(self):
        self.name=''
        while self.name in Robot.EXISTING:
            characters=Robot.generate_random_character()+Robot.generate_random_character()
            numbers=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
            self.name=characters+numbers
        Robot.EXISTING.append(self.name)
        pass
    def generate_random_character():
        return 'abcdefghijklmnopqrstuvwxyz'.upper()[randint(0, 25)]
        pass
    def reset(self):
        self.generate_random_name()
        pass