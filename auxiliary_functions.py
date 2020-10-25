import pygame

pygame.init()

MAZE_SIZE = 49
PINK = (255, 192, 203)
MAROON = (128, 0, 0)
LIGHTBLUE = (173, 216, 230)
BLACK = (0, 0, 0)
PALEVIOLETRED1 = (255, 130, 171)


def create_empty_maze(size):
    maze = []
    for i in range(size):
        if i % 2 == 0:
            maze.append(["#"] * size)
        else:
            maze.append(['#', ' '] * (size // 2))
            maze[i].append("#")
    return maze


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def mark_as_used(self, used):
        used[self.x][self.y] = True

    def is_used(self, used):
        return used[self.x][self.y]

    def path(self, maze):
        maze.arr[self.x][self.y] = "*"

    def unpath(self, maze):
        maze.arr[self.x][self.y] = " "

    def find_neighbours(self, used):
        neighbours = []
        if self.y + 2 < MAZE_SIZE and not used[self.x][self.y + 2]:
            neighbours.append(Cell(self.x, self.y + 2))
        if self.y - 2 >= 0 and not used[self.x][self.y - 2]:
            neighbours.append(Cell(self.x, self.y - 2))
        if self.x + 2 < MAZE_SIZE and not used[self.x + 2][self.y]:
            neighbours.append(Cell(self.x + 2, self.y))
        if self.x - 2 >= 0 and not used[self.x - 2][self.y]:
            neighbours.append(Cell(self.x - 2, self.y))
        return neighbours

    def find_neighbours_pathsolving(cell, maze, used):
        neighbours = []
        if cell.y + 1 < MAZE_SIZE and maze.arr[cell.x][cell.y + 1] == " " \
                and not used[cell.x][cell.y + 1]:
            neighbours.append(Cell(cell.x, cell.y + 1))
        if cell.y - 1 >= 0 and maze.arr[cell.x][cell.y - 1] == " " \
                and not used[cell.x][cell.y - 1]:
            neighbours.append(Cell(cell.x, cell.y - 1))
        if cell.x + 1 < MAZE_SIZE and maze.arr[cell.x + 1][cell.y] == " " \
                and not used[cell.x + 1][cell.y]:
            neighbours.append(Cell(cell.x + 1, cell.y))
        if cell.x - 1 >= 0 and maze.arr[cell.x - 1][cell.y] == " " \
                and not used[cell.x - 1][cell.y]:
            neighbours.append(Cell(cell.x - 1, cell.y))
        return neighbours


class Wall:
    def __init__(self, x, y, f, s):
        self.x = x
        self.y = y
        self.firstCell = f
        self.secondCell = s


class Maze:
    def __init__(self, size):
        self.arr = create_empty_maze(size)

    def draw(self, win):
        win.fill(PINK)
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if self.arr[i][j] == "#":
                    pygame.draw.rect(win, MAROON, (i * 20, j * 20, 20, 20))
                if self.arr[i][j] == " ":
                    pygame.draw.rect(win, PINK, (i * 20, j * 20, 20, 20))
                if self.arr[i][j] == "*":
                    pygame.draw.rect(win, PALEVIOLETRED1, (i * 20, j * 20, 20, 20))
