from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

class TicTacToe(GridLayout):
    def __init__(self):
        super(TicTacToe, self).__init__(cols=3, spacing=2)
        self.count = 0
        self.symbols = ('X', 'O')
        self.symbolNum = 0
        self.grid = [[None for col in range(self.cols)] for row in range(self.cols)]

        for row in range(self.cols):
            for col in range(self.cols):
                tile = Button(font_size=40, on_press = self.action)
                self.grid[row][col] = tile
                self.add_widget(tile)

    def action(self, button1):
        button1.text = self.symbols[self.symbolNum]
        self.symbolNum = (self.symbolNum + 1) % 2
        self.count += 1
        self.checkResult()

    def checkResult(self):
        winner = self.getWinner()

        if winner:
            closeButton = Button(text = '   ' + winner +' won !!\nClick here to restart')
        elif self.count == (self.cols * self.cols):
            closeButton = Button(text = 'Game finished !!\nClick here to restart')
        else:
            return

        myPopUp = Popup(title = 'Result of Game', content = closeButton, size_hint = (.5, .5))
        myPopUp.open()
        closeButton.bind(on_press = myPopUp.dismiss, on_release = self.restartGame)

    def getWinner(self):
        gridValues = [[self.grid[row][col].text for col in range(self.cols)] for row in range(self.cols)]

        for row in range(self.cols):
            result = self.sameSymbol(gridValues[row])
            if result:
                return result

        for col in range(self.cols):
            column = [row[col] for row in gridValues]
            result = self.sameSymbol(column)
            if result:
                return result

        diag = [gridValues[i][i] for i in range(self.cols)]
        result = self.sameSymbol(diag)
        if result:
            return result

        diag = [gridValues[i][(self.cols - 1) - i] for i in range(self.cols)]
        result = self.sameSymbol(diag)
        if result:
            return result

        return False

    def sameSymbol(self, valueList):
        symbol = valueList[0]
        
        for element in valueList:
            if element != symbol:
                return False
        return symbol

    def restartGame(self, btn):
        self.count = 0

        for row in range(self.cols):
            for col in range(self.cols):
                self.grid[row][col].text = ''
                

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()


def main():
    TicTacToeApp().run()


if __name__ == '__main__':
    main()
