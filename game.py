import tkinter
import random
from tkinter.messagebox import *

class Game(object):


    # Add your class variables if needed here - square size, etc...)
    square_size = 150



    def __init__(self, parent):
        parent.title('Chaitanya Sharmas Tic Tac Toe')
        self.parent = parent
        self.box = [0,1,2,3,4,5,6,7,8]
        self.player = []
        self.rival = []

        # Create the restart button widget
        restart_button = tkinter.Button(self.parent, text='RESTART', command=self.restart)
        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent, width =self.square_size * 3,height = self.square_size * 3)



        for row in range(3):
            for column in range(3):
                 self.canvas.create_rectangle(self.square_size *
                                                      column,
                                        self.square_size * row,
                                        self.square_size * (column + 1),
                                        self.square_size * (row + 1),fill =
                                        'white')
        restart_button.grid()
        self.canvas.grid()
        self.result = tkinter.Label(self.parent)
        # Create any additional instance variable you need for the game
        self.canvas.bind("<Button-1>", self.play)

    def restart(self):
        self.result.configure(text='')
        for square in self.canvas.find_all():
            self.canvas.itemconfigure(square, fill='white')
        self.canvas.bind("<Button-1>",self.play)
        self.box =[0,1,2,3,4,5,6,7,8]
        del self.player[:]
        del self.rival[:]


    def play(self, event):
        square = self.canvas.find_closest(event.x,event.y)
        if square[0]-1 in self.box:
            if square[0]-1 not in self.player and square[0]-1 not in \
                    self.rival:
                self.player.append(square[0]-1)
                self.canvas.itemconfigure(square[0],fill='red')

                if self.win_combos():
                    self.canvas.unbind("<Button-1>")
                    showinfo("Result","You have won the game!!!!")

                    self.result.grid()
                else:
                    if len(self.rival)+len(self.player) != 9:
                        self.computer()
                        if self.cpu_combos():
                            showinfo("Result","You have lost!!!!")
                            self.canvas.unbind("<Button-1>")
                            self.result.grid()
                    else:
                        showinfo("Result", "The game is tied!!!!")
                        self.canvas.unbind("<Button-1>")
                        self.result.grid()

            else:
                return


    def computer(self):
        my_int = random.randint(0, 8)
        if my_int not in self.rival and my_int not in self.player:
            self.rival.append(my_int)
            self.canvas.itemconfigure(my_int+1, fill='blue')#1-9 squares

        else:
            self.computer() #recurse

    def cpu_combos(self):
        #wins involving the first box
        if 0 in self.rival:
            #1st row win
            if 1 in self.rival and 2 in self.rival:
                return True
            #1st column win
            elif 3 in self.rival and 6 in self.rival:
                return True
            #first diagnol win
            elif 4 in self.rival and 8 in self.rival:
                return True
        #wins involving second box
        if 1 in self.rival:
            if 0 in self.rival and 2 in self.rival:
                return True
            elif 4 in self.rival and 7 in self.rival:
                return True

        #wins involving 3rd box
        if 2 in self.rival:
            if 0 in self.rival and 1 in self.rival:
                return True
            elif 5 in self.rival and 8 in self.rival:
                return True
            elif 4 in self.rival and 6 in self.rival:
                return True

        #4th box
        if 3 in self.rival:
            if 0 in self.rival and 6 in self.rival:
                return True
            elif 4 in self.rival and 5 in self.rival:
                return True
        #middle square
        if 4 in self.rival:
            if 3 in self.rival and 5 in self.rival:
                return True
            elif 1 in self.rival and 7 in self.rival:
                return True
            elif 0 in self.rival and 8 in self.rival:
                return True
            elif 2 in self.rival and 6 in self.rival:
                return True
        #6th
        if 5 in self.rival:
            if 2 in self.rival and 8 in self.rival:
                return True
            elif 3 in self.rival and 4 in self.rival:
                return True
        #7th
        if 6 in self.rival:
            if 7 in self.rival and 8 in self.rival:
                return True
            elif 4 in self.rival and 2 in self.rival:
                return True
            elif 3 in self.rival and 0 in self.rival:
                return True
        #8th
        if 7 in self.rival:
            if 6 in self.rival and 8 in self.rival:
                return True
            if 4 in self.rival and 1 in self.rival:
                return True
        if 8 in self.rival:
            if 2 in self.rival and 5 in self.rival:
                return True
            if 4 in self.rival and 0 in self.rival:
                return True
            if 6 in self.rival and 7 in self.rival:
                return True
        return False

    def win_combos(self):
        if 0 in self.player:
            if 1 in self.player and 2 in self.player:
                return True
            elif 3 in self.player and 6 in self.player:
                return True
            elif 4 in self.player and 8 in self.player:
                return True
        if 1 in self.player:
            if 0 in self.player and 2 in self.player:
                return True
            elif 4 in self.player and 7 in self.player:
                return True
        if 2 in self.player:
            if 0 in self.player and 1 in self.player:
                return True
            elif 5 in self.player and 8 in self.player:
                return True
            elif 4 in self.player and 6 in self.player:
                return True
        if 3 in self.player:
            if 0 in self.player and 6 in self.player:
                return True
            elif 4 in self.player and 5 in self.player:
                return True

        if 4 in self.player:
            if 3 in self.player and 5 in self.player:
                return True
            elif 1 in self.player and 7 in self.player:
                return True
            elif 0 in self.player and 8 in self.player:
                return True
            elif 2 in self.player and 6 in self.player:
                return True

        if 5 in self.player:
            if 2 in self.player and 8 in self.player:
                return True
            elif 3 in self.player and 4 in self.player:
                return True

        if 6 in self.player:
            if 7 in self.player and 8 in self.player:
                return True
            elif 4 in self.player and 2 in self.player:
                return True
            elif 3 in self.player and 0 in self.player:
                return True

        if 7 in self.player:
            if 6 in self.player and 8 in self.player:
                return True
            if 4 in self.player and 1 in self.player:
                return True

        if 8 in self.player:
            if 2 in self.player and 5 in self.player:
                return True
            if 4 in self.player and 0 in self.player:
                return True
            if 6 in self.player and 7 in self.player:
                return True
        return False


def main():
    parent = tkinter.Tk()
    Game(parent)
    parent.mainloop()


if __name__ == '__main__':
    main()