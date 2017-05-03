

class Ant(object):

    rules = {"white": ("black", "left"),
            "black": ("white", "right")}

    def __init__(self, x, y, color, direction):
        self.x, self.y = x, y
        self.color = color
        self.direction = direction

    def next_step(self, col):
        """
        Takes in the color of the tile the Ant is on and adjusts the Ant's position
        :param col: The color of the tile the Ant is on
        :return: self.color, the color to change the last tile to
        """
        instruction = self.rules[col]
        self.color = instruction[0]
        turn = instruction[1]
        if self.direction == 'N' and turn == 'left':
            self.x = self.x - 1
            self.direction = 'W'
        elif self.direction == 'N' and turn == 'right':
            self.x = self.x + 1
            self.direction = 'E'
        elif self.direction == 'E' and turn == 'left':
            self.y = self.y + 1
            self.direction = 'N'
        elif self.direction == 'E' and turn == 'right':
            self.y = self.y - 1
            self.direction = 'S'
        elif self.direction == 'S' and turn == 'left':
            self.x = self.x + 1
            self.direction = 'E'
        elif self.direction == 'S' and turn == 'right':
            self.x = self.x - 1
            self.direction = 'W'
        elif self.direction == 'W' and turn == 'left':
            self.y = self.y - 1
            self.direction = 'S'
        elif self.direction == 'W' and turn == 'right':
            self.y = self.y + 1
            self.direction = 'N'
        return self.color
