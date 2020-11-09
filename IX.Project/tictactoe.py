import tkinter
from tkinter import messagebox
from tictactoe_game_engine import TictactoeGameEngine
class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        print(self.game_engine)
        while True:
            row = int(input('row : '))
            col = int(input('col : '))
            self.game_engine.set(row,col)
            print(self.game_engine)
            winner = self.game_engine.check_winner()
            if winner == '0' or winner == 'x' or winner == 'd':
                break

            if winner == 'o':
                 print('o승리')

            if winner == 'x':
                 print('x승리')

            if winner == 'd':
                print('무승부')


class Tictactoe_GUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        
        ##창의 기본적으로 생성
        CANVAS_SIZE = 300 #창의 크기
        self.TILE_SIZE = CANVAS_SIZE / 3
        
        ##창 생성
        self.root = tkinter.Tk() #창
        self.root.geometry(str(CANVAS_SIZE) + 'x' + str(CANVAS_SIZE)) #속성값을 문자열로 보냄
        self.root.title('틱 택 토') #창의 이름을 바꿔주는 것 
        self.root.resizable(width = False, height = False) #사이즈를 바꿀 수 있는지 묻는 중
        self.canvas = tkinter.Canvas(self.root, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE) #창, 넓이, 길이등 설정
        self.canvas.pack() #다른 요소가 없으면 이대로 실행
        
        ##이미지 생성
        self.images = {} #{'O' : photoImages 객체 (O.gif) }로 딕셔너리로 저장이 된다
        self.images['O'] = tkinter.PhotoImage(file = 'O.gif') #이미지 생성
        self.images['X'] = tkinter.PhotoImage(file='X.gif')  #gif만 지원이 가능함

        self.canvas.bind('<Button-1>', self.click_handler) #버튼 지정

    def click_handler(self, event):
        x = event.x
        y = event.y

        col = x // 100 + 1
        row = y // 100 + 1

        self.game_engine.set(row, col)
        #print(self.game_engine)
        self.draw_board()
        
        if self.game_engine.check_winner() == 'o':
            messagebox.showinfo('Game Over','O가 이김.')
            self.root.quit() #종료하는 창

        elif self.game_engine.check_winner() == 'x':
            messagebox.showinfo('Game Over','X가 이김.')
            self.root.quit()

        elif self.game_engine.check_winner() == 'd':
            messagebox.showinfo('Game Over','무승부')
            self.root.quit()

    def draw_board(self):
        #self.game_engine.board
        x = 0
        y = 0

        for i , v in enumerate(self.game_engine.board):
           if v == 'x':
               self.canvas.create_image(x, y, anchor='nw', image=self.images['X'])
           elif v == 'o':
               self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])

           x += self.TILE_SIZE
           if i % 3 == 2:
             x = 0
             y += self.TILE_SIZE


            # if v != '.':
            #     self.canvas.create_image(x, y, anchor='nw', image=self.images['v'])



    def play(self):
        # self.canvas.create_image(200, 100, anchor = 'nw',image = self.images['O']) #가운데 점을 100,100으로 맞추고, 'O'사진이 나온
        # self.canvas.create_image(0, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(100, 200, anchor='nw', image=self.images['O'])

        # self.canvas.create_image(0, 0, anchor = 'nw',image = self.images['X'])
        # self.canvas.create_image(200, 0, anchor='nw', image=self.images['X'])
        self.root.mainloop() #윈도우 창을 실행하게 해 줌

if __name__ == '__main__':
    #ttt = Tictactoe()
    ttt = Tictactoe_GUI()
    ttt.play()