class Parabola:
    @staticmethod
    def help():
        import formatkit
        return f"""{formatkit.default}Welcome to MathFramework 1.5.3{formatkit.default}
        ├ __init__ - [a, b, c] accept a, b, c coefficients of parabola
        ├ table(min, max) - [Minimum x, Maximum x]  build table f(x)=y
        └ description() - all information about current parabola
✔ This class is singled out as independent, but is still a member of MathFramework
        """

    def __init__(self, a: int, b: int, c: int):
        from src.quadratic_equation import quadratic_equation
        self.a = a
        self.b = b
        self.c = c
        self.branches = 'up' if self.a >= 1 else 'down'
        self.x_vertex = (-self.b)/2*self.a
        self.y_vertex = self.a*self.x_vertex**2+self.b*self.x_vertex+self.c
        self.zeros_x  = quadratic_equation(self.a, self.b, self.c)
        self.zeros_y = self.a*self.zeros_x[0]**2+self.b*self.zeros_x[0]+self.c, self.a*self.zeros_x[1]**2+self.b*self.zeros_x[1]+self.c

    def table(self, min, max, draw=True):
        from beautifultable import BeautifulTable
        import matplotlib.pyplot as plt
        from math import sqrt, pow
        plt.style.use('seaborn-darkgrid')
        fig, ax = plt.subplots()
        x_values = [x for x in range(min, max)]
        y_values = []
        table = BeautifulTable()
        for x in range(min, max):
            y = self.a*x**2+self.b*x+self.c
            y_values.append(y)
            table.rows.append([x, y])
        table.columns.header = ["x", "f(x)"]
        ax.plot(x_values, y_values)
        plt.show()
        return table
    def description(self):
        return f"""\nThis parabola {self.a}x²+{self.b}x+{self.c} has:
        ├ {self.branches} branches
        ├ vertex at ({self.x_vertex}, {self.y_vertex})
        └ zeros are ({self.zeros_x[0]}, {self.zeros_y[0]}) and ({self.zeros_x[1]}, {self.zeros_y[1]})"""