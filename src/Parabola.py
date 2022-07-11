class Parabola:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        self.branches = 'up' if self.a >= 1 else 'down'
        self.x_vertex = (-self.b)/2*self.a
        self.y_vertex = self.a*self.x_vertex**2+self.b*self.x_vertex+self.c

    def table(self, min, max):
        for x in range(min, max):
            y = self.a*x**2+self.b*x+self.c
            print(x, y)
    def description(self):
        return f"""\nThis parabola {self.a}x²+{self.b}x+{self.c} has:
        ├ {self.branches} branches
        ├ vertex at ({self.x_vertex}, {self.y_vertex})"""