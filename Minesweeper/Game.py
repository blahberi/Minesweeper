import random

class __Board:
    def __init__(self, dim):
        self.dim = dim
        self.board = [] # board has numbers which indicate how many bombs are around
        """ extra numbers:
        10 bomb
        11 not revealed
        12 flag
        13 question mark
        """
        for i in range(self.dim[1]):
            self.board.append([])
        for row in self.board:
            for i in range(dim[0]):
                row.append(11)


class Game(__Board):
    def __init__(self, dim, bombs_amount):
        super().__init__(dim)
        self.bombs_amount = bombs_amount
        self.didSelect = False
        self.GAME_OVER = False

    def select(self, location):
        if self.board[location[1]][location[0]] != 11:
            return
        if self.GAME_OVER:
            return
        if not self.didSelect:
            self.__create_bombs(location)
            self.didSelect = True
        if location in self.bombs:
            self.GAME_OVER = True
        bomb_count = 0
        x_list_temp = (location[0] - 1, location[0], location[0] + 1)
        y_list_temp = (location[1] - 1, location[1], location[1] + 1)
        x_list = []
        y_list = []
        for x in x_list_temp:
            if x >= 0 and x < self.dim[0]:
                x_list.append(x)
        for y in y_list_temp:
            if y >= 0 and y < self.dim[1]:
                y_list.append(y)

        for x in x_list:
            for y in y_list:
                if (x, y) in self.bombs:
                    bomb_count += 1
        self.board[location[1]][location[0]] = bomb_count
        if bomb_count == 0:
            for x in x_list:
                for y in y_list:
                    self.select((x, y))
        return

    def __create_bombs(self, location):
        # create bombs
        self.bombs = []
        x_list_temp = (location[0] - 1, location[0], location[0] + 1)
        y_list_temp = (location[1] - 1, location[1], location[1] + 1)
        x_list = []
        y_list = []
        for x in x_list_temp:
            if x >= 0 and x <=self.dim[0]:
                x_list.append(x)
        for y in y_list_temp:
            if y >= 0 and y <= self.dim[1]:
                y_list.append(y)
        for i in range(self.bombs_amount):
            while True:
                x = random.randint(0, self.dim[0])
                y = random.randint(0, self.dim[1])
                if x not in x_list or y not in y_list:
                    if (x, y) not in self.bombs:
                        self.bombs.append((x, y))
                        break
        return

    def __str__(self):
        res = ''
        for row in self.board:
            for square in row:
                res += f'{square} '
            res += '\n'
        return res
