""" my code to robot-name exercise """
from string import ascii_uppercase,  digits
from random import choices

class Robot:
    """ Create a robot with a random and uinique name """
    robots_name = set()

    def __init__(self):
        name_exist = True
        # verifica se o nome do robo ja existe
        while name_exist:
            characters= choices(ascii_uppercase, k=2) + choices(digits, k=3)
            check_name = ''.join(item for item in characters)
            if check_name not in Robot.robots_name:
                Robot.robots_name.add(check_name)
                self.name = check_name
                name_exist = False
    
    def __repr__(self) -> str:
        return self.name

    def reset(self):
        """ reset the robot """
        return self.__init__()