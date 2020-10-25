from auxiliary_functions import Cell, Wall, Maze
import auxiliary_functions
import window
from random import randint
import pygame

pygame.init()


def generate_prim(win):
    maze = Maze(auxiliary_functions.MAZE_SIZE)
    used = [[False] * auxiliary_functions.MAZE_SIZE for i in range(auxiliary_functions.MAZE_SIZE)]

    used[1][1] = True
    wall_list = [Wall(2, 1, Cell(1, 1), Cell(3, 1)), Wall(1, 2, Cell(1, 1), Cell(1, 3))]
    while len(wall_list) > 0:
        w = wall_list[randint(0, len(wall_list) - 1)]
        if not (w.firstCell.is_used(used) and w.secondCell.is_used(used)):
            maze.arr[w.x][w.y] = " "
            if not w.firstCell.is_used(used):
                cur_cell = w.firstCell
            else:
                cur_cell = w.secondCell
            cur_cell.mark_as_used(used)
            neighbours = cur_cell.find_neighbours(used)
            for next_cell in neighbours:
                new_wall = Wall(cur_cell.x + (next_cell.x - cur_cell.x) // 2,
                               cur_cell.y + (next_cell.y - cur_cell.y) // 2,
                               cur_cell, next_cell)
                wall_list.append(new_wall)
        wall_list.remove(w)

        pygame.time.delay(3)
        maze.draw(win)
        window.update_win(win)
    return maze
