import random


class Game2048:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.add_new()
        self.add_new()

    def add_new(self):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_positions:
            i, j = random.choice(empty_positions)
            self.grid[i][j] = 2

    def print_board(self):
        # self.clear_screen()
        for row in self.grid:
            print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
        print()

    def move_left(self):
        for i in range(4):
            row = self.grid[i]
            while True:
                row_after_move = [cell for cell in row if cell != 0]
                row_after_move += [0] * (4 - len(row_after_move))
                for j in range(3):
                    if row_after_move[j] == row_after_move[j + 1]:
                        row_after_move[j] *= 2
                        row_after_move[j + 1] = 0
                self.grid[i] = row_after_move
                if row == row_after_move:
                    break
                row = row_after_move.copy()


    def move(self, direction):
        assert direction in ['w', 'a', 's', 'd']
        if direction == 'a':
            self.move_left()
        elif direction == 'd':
            for i in range(4):
                self.grid[i] = list(reversed(self.grid[i]))
            self.move_left()
            for i in range(4):
                self.grid[i] = list(reversed(self.grid[i]))
        elif direction == 'w':
            self.grid = [list(row) for row in zip(*self.grid)]
            self.move_left()
            self.grid = [list(row) for row in zip(*self.grid)]
        elif direction == 's':
            self.grid = [list(row) for row in zip(*self.grid)]
            for i in range(4):
                self.grid[i] = list(reversed(self.grid[i]))
            self.move_left()
            for i in range(4):
                self.grid[i] = list(reversed(self.grid[i]))
            self.grid = [list(row) for row in zip(*self.grid)]

    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
                if i > 0 and self.grid[i][j] == self.grid[i - 1][j]:
                    return False
                if j > 0 and self.grid[i][j] == self.grid[i][j - 1]:
                    return False
        return True

    def play_game(self):
        while True:
            self.print_board()
            direction = input("Enter direction (w, a, s, d) or 'q' to quit: ").lower()

            if direction == 'q':
                print("Quitting the game. Goodbye!")
                break

            try:
                self.move(direction)
                self.add_new()

                if self.is_game_over():
                    self.print_board()
                    print("Game over! No more moves left.")
                    break

            except AssertionError:
                print("Invalid input. Please enter a valid direction.")
