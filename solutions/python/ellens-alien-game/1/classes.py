"""Solution to Ellen's Alien Game exercise."""


class Alien():
    """Create an Alien object with location x_coordinate and y_coordinate. """

    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x_coordinate: int = x_coordinate
        self.y_coordinate: int = y_coordinate
        self.health: int = 3



    # (class)total_aliens_created: int
    def hit(self):
        """ Decrement Alien health by one point """
        self.health -= 1

    def is_alive(self):
        """ Return a boolean for if Alien is alive (if health is > 0) """
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        """ Move Alien object to new coordinates. """
        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate

    def collision_detection(self, other):
        """ detect when such a collision has occurred """
        pass

def new_aliens_collection(aliens_coordinate: list):
    """ create a list of alien objects """

    return [Alien(item[0], item[1]) for item in aliens_coordinate]
