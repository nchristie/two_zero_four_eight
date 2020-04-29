#!/usr/bin/python3

from random import randint
import copy
from time import sleep
from ascii_art_numbers import ASCII_ART_NUMBERS

KEY = {"A": "left", "D": "right", "W": "up", "S": "down", "B": "back"}

def main():
    print("\nLeft=A, Right=D, Up=W, Down=S")
    grid = FourByFourGrid()
    grid.add_new_number(2)
    grid.print_grid()
    while True:
        grid = get_and_make_move(grid)
        choose_four = 15
        rand_num = randint(0, choose_four)
        if rand_num == choose_four:
            grid.add_new_number(4)
        else:
            grid.add_new_number(2)
        grid.has_new_high()
        grid.print_grid()

    print(f"Game Over")

def get_and_make_move(grid):
    while True:
        try:
            move = get_move()
            grid.make_move(move)
            return grid
        except Exception as e:
            print(e)
            grid.print_grid()

def get_move():
    allowed_moves = ["A", "D", "W", "S", "B"]
    move = input("Your move:\n").upper()
    if move == "Q":
        exit()
    if move not in allowed_moves:
        get_move()
    print(f"\n{KEY[move]}\n")
    return move


class FourByFourGrid:
    def __init__(self):
        self.min_index = 0
        self.max_index = 3
        self.grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.moves = {
            "A": self.left_move,
            "D": self.right_move,
            "W": self.up_move,
            "S": self.down_move,
            "B": self.back_move,
        }
        self.grid_history = []
        self.highest_number = 2

    def has_new_high(self):
        for row in self.grid:
            for number in row:
                if number > self.highest_number:
                    self.highest_number = number
                    print(f"Congratulations, you've reached a new high of {number}")
                    if ASCII_ART_NUMBERS.get(number):
                        print(ASCII_ART_NUMBERS.get(number))
                        sleep(1)

    def print_grid(self):
        for row in self.grid:
            for item in row:
                str_item = str(item)
                if str_item == "0":
                    str_item = "  "
                if len(str_item) < 4:
                    str_item+=(" "*(4-len(str_item)))
                print(str_item, end=" | ")
            print("\n")

    def add_new_number(self, number):
        x = randint(self.min_index, self.max_index)
        y = randint(self.min_index, self.max_index)
        if self.grid[x][y]:
            self.add_new_number(number)
        else:
            self.grid[x][y] = number

    def make_move(self, move):
        start_state = copy.deepcopy(self.grid)
        self.moves[move]()
        end_state = copy.deepcopy(self.grid)
        self.grid_history.append(end_state)
        if self.grid == start_state:
            raise Exception(f"{KEY[move]} move not possible, try another")

    def back_move(self):
        self.grid = self.grid_history.pop()
        self.grid = self.grid_history.pop()

    def left_move(self):
        for i, row in enumerate(self.grid):
            self.grid[i] = left_move_row(row)


    def right_move(self):
        for row in self.grid:
            row.reverse()
        self.left_move()
        for row in self.grid:
            row.reverse()

    def up_move(self):
        self.transpose()
        self.left_move()
        self.transpose()


    def down_move(self):
        self.transpose()
        self.right_move()
        self.transpose()


    def transpose(self):
        new_grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],   
        ]
        for i, row in enumerate(self.grid):
            for j, item in enumerate(row):
                new_grid[j][i] = item
        self.grid = new_grid


def left_move_row(row):
    for i in range(len(row)-1):
        row = shift_zeroes(row)
        row[i], row[i+1] = calculate_new_values(row[i], row[i+1])
    return row

def calculate_new_values(a, b):
    if a == b:
        a *= 2
        b = 0
    return a, b

def shift_zeroes(row):
    new_row = []
    for item in row:
        if item != 0:
            new_row.append(item)
    
    diff = len(row) - len(new_row)
    if diff > 0:
        for i in range(diff):
            new_row.append(0)

    return new_row

if __name__ == "__main__":
    main()
