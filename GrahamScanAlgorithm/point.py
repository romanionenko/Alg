class Point:
    """Represents point on a plane. Key is added """

    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

    def get_key(self):
        return self.key

    def get_x(self):
        """Returns point's X Axis value"""
        return self.x

    def get_y(self):
        """Returns point's Y Axis value"""
        return self.y

    def __str__(self):
        def to_float(number): return int(number) if number.is_integer() else number
        return str(self.key) + ',\t' + str(to_float(self.x)) + ',\t' + str(to_float(self.y))

    def __lt__(self, other): return self.y < other.y if (self.x == other.x) else self.x < other.x

    def __eq__(self, other): return self.x == other.x and self.y == other.y
