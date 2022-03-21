"""Solution to Ellen's Alien Game exercise."""


class Alien():
    """Create an Alien object with location x_coordinate and y_coordinate. """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1

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
        # return (self.x_coordinate, self.y_coordinate) == (other.x_coordinate, other.y_coordinate)

def new_aliens_collection(aliens_coordinate: list):
    """ create a list of alien objects """

    return [Alien(item[0], item[1]) for item in aliens_coordinate]
