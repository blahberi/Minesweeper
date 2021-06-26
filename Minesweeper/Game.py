import random

class __Board:
    def __init__(self, dim):
        self.dim = dim
        self.board = [] # board has numbers which indicate how many bombs are around
        """ extra numbers:
        10 not revealed
        11 flag
        12 question mark
        """
        for i in range(self.dim[0]):
            self.board.append([])
        for row in self.board:
            for i in range(dim[1]):
                row.append(10)


class Game(__Board):
    def __init__(self, dim, bombs_amount):
        super().__init__(dim)
        self.bombs_amount = bombs_amount
        self.didSelect = False
        self.GAME_OVER = False

    def select(self, location):
        if not self.GAME_OVER:
            if not self.didSelect:
                self.__create_bombs()
                self.didSelect = False
            if location in self.bombs:
                print('oops you selected a bomb GAME OVER')
                self.GAME_OVER = True
                return
            bomb_count = 0
            x_list_temp = (location[0] - 1, location[0], location[0] + 1)
            y_list_temp = (location[1] - 1, location[0], location[0] + 1)
            x_list = []
            y_list = []
            for x in x_list_temp:
                if x >= 0:
                    x_list.append(x)
            for y in y_list_temp:
                if y >= 0:
                    y_list.append(y)

            for x in x_list:
                for y in y_list:


    def __create_bombs(self):
        # create bombs
        self.bombs = []
        for i in range(self.bombs_amount):
            x = random.randint(0, self.dim[0])
            y = random.randint(0, self.dim[1])
            self.bombs.append((x, y))

    def __str__(self):
        res = ''
        for row in self.board:
            for square in row:
                res += f'{square} '
            res += '\n'
        return res
