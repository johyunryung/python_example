class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)
        self.current_turn = 'x'

    def get(self, row, col):
        row -= 1
        col -= 1
        return self.board[row * 3 + col]

    def set(self, row, col):
        if row < 1 and row > 3:
            return

        if col < 1 and col > 3:
            return

        row -= 1
        col -= 1
        self.board[row * 3 +col] = self.current_turn
        self.current_turn = 'o' if self.current_turn == 'x' else 'x'
        # lf.current_turn == 'x':
        #   self.current_turn = 'o'
        # else:
        #    self.current_turn = 'x'

    def check_winner(self):
        for i in range (1, 3 + 1):
            if self.get(i,1) == self.get(i,2) == self.get(i,3) !='.':
                return self.get(i,1)

        if self.get(1,i) == self.get(2,i) == self.get(3,i) != '.':
                return self.get(1,i)

        if self.get(1,3) == self.get(2,2) == self.get(3,1) != '.':
            return self.get(2.2)

        if self.get(1,1) == self.get(2,2) == self.get(3,3) != '.':
            return self.get(2.2)

        if not '.' in self.board:
            return 'd'


    def __str__(self):
        s = ''
        for i , v in enumerate(self.board):
            s += v + '\t'
            if i % 3 ==2:
                s += '\n'
        return s

if __name__  == '__main__':
   ttt_game_engin = TictactoeGameEngine()
   print(ttt_game_engin)

   ttt_game_engin.set(2,2)
   print(ttt_game_engin)
   print(ttt_game_engin.check_winner())
   ttt_game_engin.set(1,1)
   print(ttt_game_engin)
   print(ttt_game_engin.check_winner())
   ttt_game_engin.set(2,1)
   print(ttt_game_engin)
   print(ttt_game_engin.check_winner())
   ttt_game_engin.set(1,2)
   print(ttt_game_engin)
   print(ttt_game_engin.check_winner())
   ttt_game_engin.set(2,3)
   print(ttt_game_engin)
   print(ttt_game_engin.check_winner())

