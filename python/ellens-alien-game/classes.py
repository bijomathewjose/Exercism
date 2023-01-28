"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.
    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created=0
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        self.health=3
        Alien.total_aliens_created+=1
        pass
    def hit(self):
        self.health=max(0,self.health-1)
        pass
    def is_alive(self):
        return self.health>0
    def teleport(self,x_coordinate,y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        pass
    def collision_detection(self,other_object):
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    aliens=(Alien(x_coordinate,y_coordinate) for (x_coordinate,y_coordinate) in alien_start_positions)
    return aliens
