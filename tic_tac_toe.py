class TicTacToe():
    winner_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                         (1, 4, 7), (2, 5, 8), (3, 6, 9),
                         (1, 5, 9), (3, 5, 7))

    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.score = {
            True: [],
            False: [],
        }
        self.player_flag = True
        self.rounds = 0
        self.print_board()
        
    def reset(self):
        self.__init__()

    def print_board(self):
        print('-'*9)
        for i in range (3):
            line='| '
            for j in range (3):
                line=line+str(self.board[i][j])+' '
            line=line+'|'
            print(line)
        print('-'*9)

    def turn(self, cell):
        marker = 'X' if self.player_flag else 'O'
        if cell.isdecimal():
            cell = int(cell)
            if 1 <= cell <= 9:
                pass
            else:
                return('ValError')
        else:
            return('ValError')
        isoccupied = self.check_identity(cell)
        if isoccupied:
            return 'CellOccupied'
        self.rounds += 1
        self.score[self.player_flag].append(cell)
        cell -= 1
        self.board[cell // 3][cell % 3] = marker
        self.player_flag = not self.player_flag
        self.print_board()
        is_end = self.check()
        if is_end:
            return is_end

    def check_identity(self, cell):
        for _, value in self.score.items():
            if cell in value:
                return True
        return False

    def check(self):
        msg = 'Player number {} won'
        for key, value in self.score.items():
            for condition in self.winner_conditions:
                if len(set(sorted(value)).intersection(condition)) == 3:
                    player = 1 if key else 2
                    print(msg.format(player))
                    return True
        if self.rounds == 9:
            print('Drawn game')
            return 'Drawn game'
        else:
            return False

    def game(self):
        i = 0
        while self.rounds <= 8:
            cell = input()
            res = self.turn(cell)
            if res == 'CellOccupied':
                print('Cell is occupied. Please reenter position - ')
                continue
            elif res == 'ValError':
                print('Invalid input. Please, reenter position - ')
                continue
            elif res:
               return 'Game over'