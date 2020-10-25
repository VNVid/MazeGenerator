from auxiliary_functions import Cell, Maze
import auxiliary_functions
import window
from collections import deque
from random import randint
import pygame

pygame.init()


def generate_dfs(win):
    maze = Maze(auxiliary_functions.MAZE_SIZE)
    used = [[False] * auxiliary_functions.MAZE_SIZE for i in range(auxiliary_functions.MAZE_SIZE)]

    used[1][1] = True
    unvisited_num = (auxiliary_functions.MAZE_SIZE // 2) ** 2 - 1
    cur_cell = Cell(1, 1)
    stack = deque()
    while unvisited_num > 0:
        neighbours = cur_cell.find_neighbours(used)
        if len(neighbours) > 0:
            nextCell = neighbours[randint(0, len(neighbours) - 1)]
            maze.arr[cur_cell.x + (nextCell.x - cur_cell.x) // 2][cur_cell.y + (nextCell.y - cur_cell.y) // 2] = " "
            stack.append(cur_cell)
            cur_cell = nextCell
            cur_cell.mark_as_used(used)
            unvisited_num -= 1
        elif len(stack) > 0:
            cur_cell = stack.pop()

        pygame.time.delay(3)
        maze.draw(win)
        window.update_win(win)
    return maze
