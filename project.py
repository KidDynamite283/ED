class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles

class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move(self):
        new_x, new_y = self.x, self.y
        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'W':
            new_x -= 1

        if not self.grid.has_obstacle(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No Obstacles detected."

class MoveCommand:
    def execute(self, rover):
        rover.move()

class TurnLeftCommand:
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand:
    def execute(self, rover):
        rover.turn_right()

class CommandInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self, rover):
        for command in self.commands:
            command.execute(rover)

grid = Grid(10, 10)
grid.add_obstacle(2, 2)
grid.add_obstacle(3, 5)

rover = Rover(0, 0, 'N', grid)

command_invoker = CommandInvoker()
commands = ['M', 'M', 'R', 'M', 'L', 'M']
for command in commands:
    if command == 'M':
        command_invoker.add_command(MoveCommand())
    elif command == 'L':
        command_invoker.add_command(TurnLeftCommand())
    elif command == 'R':
        command_invoker.add_command(TurnRightCommand())

command_invoker.execute_commands(rover)

status_report = rover.status_report()

print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
print(status_report)
