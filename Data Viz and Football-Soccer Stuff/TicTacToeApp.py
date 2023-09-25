import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config



Config.set('graphics', 'resizable', True)


class PvpScreen(Screen):
    def __init__(self, **kwargs):
        super(PvpScreen, self).__init__(**kwargs)

        vb = BoxLayout(orientation='vertical')
        hb = BoxLayout(orientation='horizontal')
        fl = FloatLayout()

        self.labl1 = Label(text = '[b][i]TicTacToe[/i][/b]', color = [0.41, 0.42, 0.74, 1], size_hint = (1, .35), pos_hint = {'x':0, 'y':.65}, font_size = '100sp', markup = True)
        fl.add_widget(self.labl1)

        self.labl2 = Label(text = '[b]MODE: [color=#ff0000]Player[/color] vs [color=#3385ff]Player[/color][/b]', size_hint = (1, .15), pos_hint = {'x':0, 'y':.5}, font_size = '40sp', markup = True)
        fl.add_widget(self.labl2)

        self.lab1 = Label(text = '[b][i]Enter your name Player One: [/i][/b]', size_hint = (.1, .05), pos_hint = {'x':0.1, 'y':0.4}, markup = True)
        fl.add_widget(self.lab1)
        self.txt1 = TextInput(multiline = False, size_hint = (.65, .05), pos_hint = {'x':0.30,'y':0.4})
        fl.add_widget(self.txt1)

        self.lab2 = Label(text = '[b][i]Enter your name Player Two: [/i][/b]', size_hint = (.1, .05), pos_hint = {'x':0.1, 'y':0.3}, markup = True)
        fl.add_widget(self.lab2)
        self.txt2 = TextInput(multiline = False, size_hint = (.65, .05), pos_hint = {'x':0.30,'y':0.3})
        fl.add_widget(self.txt2)

        self.btn1 = Button(text = '[b][i][font=arial]ASSIGN SYMBOLS[/b]', size_hint = (1,.1), pos_hint = {'x':0,'y':0.1}, background_color = [0.14,0.43,0.91,1], font_size = '50sp', markup = True)
        self.btn1.bind(on_press = self.assign)
        fl.add_widget(self.btn1)

        self.btn2 = Button(text = '[b][font=impact]START', markup = True, font_size = '50sp', size_hint = (.5,.1), pos_hint = {'x':0,'y':0}, disabled = True, background_color = [0.2,1,0.2,1])
        self.btn2.bind(on_press = self.changer)
        fl.add_widget(self.btn2)
        
        self.btn3 = Button(text = '[b][font=impact]QUIT', markup = True, font_size = '50sp', size_hint = (.5,.1), pos_hint = {'x':0.5,'y':0}, background_color = [1,0,0,1])
        self.btn3.bind(on_press = self.quit_changer)
        fl.add_widget(self.btn3)

        self.add_widget(hb)
        self.add_widget(vb)
        self.add_widget(fl)

    def enable(self, btn):
        self.btn2.disabled = False

    def changer(self, *args):
        vb = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=3)

        self.count = 0

        self.ba = Button(text="[color=#000000][b]RESTART[/b][/color]", background_color = [0.4,0.8,1,1], markup = True, font_size = '25sp')
        self.ba.bind(on_press = self.restarter)
        gl.add_widget(self.ba)

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = self.txt2.text

        self.bb = Button(text=f"[color=#000000][b][i]{first}'s turn [X]:[/i][/b][/color]", disabled = False, background_color = [0.2, 1, 0.2, 1], markup = True, font_size = '25sp')
        gl.add_widget(self.bb)

        self.bc = Button(text='[color=#000000][b]QUIT[/b][/color]', markup = True, font_size = '25sp', background_color = [1,0,0,1])
        self.bc.bind(on_press = self.quit_changer)
        gl.add_widget(self.bc)                

        self.b1 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b1.bind(on_press = self.sign)
        gl.add_widget(self.b1)
        
        self.b2 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b2.bind(on_press = self.sign)
        gl.add_widget(self.b2)
        
        self.b3 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b3.bind(on_press = self.sign)
        gl.add_widget(self.b3)
        
        self.b4 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b4.bind(on_press = self.sign)
        gl.add_widget(self.b4)
        
        self.b5 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b5.bind(on_press = self.sign)
        gl.add_widget(self.b5)
        
        self.b6 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b6.bind(on_press = self.sign)
        gl.add_widget(self.b6)
        
        self.b7 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b7.bind(on_press = self.sign)
        gl.add_widget(self.b7)
        
        self.b8 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b8.bind(on_press = self.sign)
        gl.add_widget(self.b8)
        
        self.b9 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b9.bind(on_press = self.sign)
        gl.add_widget(self.b9)

        self.add_widget(gl)
        self.add_widget(vb)

    def restarter(self, btn):

        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = self.txt2.text

        self.bb.text = f"[color=#000000][b][i]{first}" + "'s turn [X]:[/i][/b][/color]"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

    def sign(self, btn):
        
        self.count += 1

        if self.P1 == 'X':
            first = self.txt1.text
            second = self.txt2.text
        else:
            first = self.txt2.text
            second = self.txt1.text

        if self.count % 2 == 0:
            self.symsign = 'O'
            self.bb.text = first+"'s turn [X]:"
        else:
            self.symsign = 'X'
            self.bb.text = second+"'s turn [O]:"

        btn.text = self.symsign
        if self.check():
            self.winner()
        elif self.count == 9:
            self.draw()

    def texter(self):
        if self.count % 2 == 0:
            return "X"
        else:
            return "O"

    def winreset(self,btn):
        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = self.txt2.text

        self.bb.text = first+"'s turn [X]:"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

        self.winpop.dismiss()

    def drawreset(self,btn):
        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = self.txt2.text

        self.bb.text = first+"'s turn [X]:"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

        self.drawpop.dismiss()

    def winner(self):
        button1 = Button(text = f"{self.symsign} is the winner!\nPress to RESET.")
        button1.bind(on_press = self.winreset)
        self.winpop = Popup(title = 'Result of Game: ', content = button1,  size_hint = (.5, .5))
        self.winpop.open()

    def draw(self):
        button1 = Button(text = f"      Draw!\nPress to RESET.")
        button1.bind(on_press = self.drawreset)
        self.drawpop = Popup(title = 'Result of Game: ', content = button1, size_hint = (.5, .5))
        self.drawpop.open()

    def check(self):

        '''Function to check all the winning conditions.'''
        
        if self.b1.text == self.symsign and self.b2.text == self.symsign and self.b3.text == self.symsign:
            return True
        if self.b4.text == self.symsign and self.b5.text == self.symsign and self.b6.text == self.symsign:
            return True
        if self.b7.text == self.symsign and self.b8.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b1.text == self.symsign and self.b4.text == self.symsign and self.b7.text == self.symsign:
            return True
        if self.b2.text == self.symsign and self.b5.text == self.symsign and self.b8.text == self.symsign:
            return True
        if self.b3.text == self.symsign and self.b6.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b1.text == self.symsign and self.b5.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b3.text == self.symsign and self.b5.text == self.symsign and self.b7.text == self.symsign:
            return True

    def assign(self, btn):
        self.t1 = self.txt1.text
        self.t2 = self.txt2.text

        if self.nameChecker():
            symbol = ['X', 'O']
        
            self.P1 = random.choice(symbol)
            if self.P1 == 'X':
                self.P2 = 'O'
            else:
                self.P2 = 'X'

            button1 = Button(text = f"         {self.t1} has {self.P1}.\n         {self.t2} has {self.P2}.\nPress to continue !!!")
            button1.bind(on_press = self.assignp)
            button1.bind(on_press = self.enable)
            self.asspop = Popup(title = 'Symbol Assignment', content = button1, size_hint = (.5, .5))
            self.asspop.open()
        else:
            button2 = Button(text = 'Please enter a valid name.')
            button2.bind(on_press = self.namep)
            self.namepop = Popup(title = 'WARNING!', content = button2, size_hint = (.5,.5))
            self.namepop.open()

    def nameChecker(self):
        flag = False

        if self.txt1.text and self.txt2.text not in ('', ' '):
            flag = True
        return flag

    def assignp(self,btn):
        self.asspop.dismiss()

    def namep(self,btn):
        self.namepop.dismiss()

    def quit_changer(self, *args):
        self.manager.current = 'menu'


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        vb = BoxLayout(orientation='vertical')
        hb = BoxLayout(orientation='horizontal')

        btn1 = Button(text = '[color=#262626][b][font=calibri][size=55]Welcome to the TicTacToe Game[/size][/font][/color]\n\
                                                            [i][size=30]Click to continue...[/size][/i][/b]', markup = True, background_color = [0.6,1,1,1])
        btn1.bind(on_press = self.changer)
        vb.add_widget(btn1)

        
        self.add_widget(vb)

    def changer(self, *args):
        self.manager.current = 'menu'


class CompEScreen(Screen):
    def __init__(self, **kwargs):
        super(CompEScreen, self).__init__(**kwargs)

        fl = FloatLayout()

        self.labl1 = Label(text = '[b][i]TicTacToe[/i][/b]', color = [0.41, 0.42, 0.74, 1], size_hint = (1, .35), pos_hint = {'x':0, 'y':.65}, font_size = '100sp', markup = True)
        fl.add_widget(self.labl1)

        self.labl2 = Label(text = '[b]MODE: [color=#ff0000]Player[/color] vs [color=#3385ff]Computer [EASY][/color][/b]', size_hint = (1, .15), pos_hint = {'x':0, 'y':.5}, font_size = '40sp', markup = True)
        fl.add_widget(self.labl2)

        self.lab1 = Label(text = '[b][i]Enter your name Player: [/i][/b]', size_hint = (.1, .05), pos_hint = {'x':0.1, 'y':0.4}, markup = True)
        fl.add_widget(self.lab1)
        self.txt1 = TextInput(multiline = False, size_hint = (.65, .05), pos_hint = {'x':0.30,'y':0.4})
        fl.add_widget(self.txt1)

        self.btn1 = Button(text = '[b][i][font=arial]ASSIGN SYMBOLS[/b]', size_hint = (1,.1), pos_hint = {'x':0,'y':0.1}, background_color = [0.14,0.43,0.91,1], font_size = '50sp', markup = True)
        self.btn1.bind(on_press = self.assign)
        fl.add_widget(self.btn1)

        self.btn2 = Button(text = '[b][font=impact]START', markup = True, font_size = '50sp', size_hint = (.5,.1), pos_hint = {'x':0,'y':0}, disabled = True, background_color = [0.2,1,0.2,1])
        self.btn2.bind(on_press = self.changer)
        fl.add_widget(self.btn2)
        
        self.btn3 = Button(text = '[b][font=impact]QUIT', markup = True, font_size = '50sp', size_hint = (.5,.1), pos_hint = {'x':0.5,'y':0}, background_color = [1,0,0,1])
        self.btn3.bind(on_press = self.quit_changer)
        fl.add_widget(self.btn3)

        self.add_widget(fl)

    def quit_changer(self, *args):
        self.manager.current = 'menu'

    def changer(self, *args):
        vb = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=3)

        self.count = 0

        self.ba = Button(text="[color=#000000][b]RESTART[/b][/color]", background_color = [0.4,0.8,1,1], markup = True, font_size = '25sp')
        self.ba.bind(on_press = self.restarter)
        gl.add_widget(self.ba)

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = "Computer"

        self.bb = Button(text=f"[color=#000000][b][i]{first}'s turn [X]:[/i][/b][/color]", disabled = False, background_color = [0.2, 1, 0.2, 1], markup = True, font_size = '25sp')
        gl.add_widget(self.bb)

        self.bc = Button(text='[color=#000000][b]QUIT[/b][/color]', markup = True, font_size = '25sp', background_color = [1,0,0,1])
        self.bc.bind(on_press = self.quit_changer)
        gl.add_widget(self.bc)                

        self.b1 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b1.bind(on_press = self.sign)
        gl.add_widget(self.b1)
        
        self.b2 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b2.bind(on_press = self.sign)
        gl.add_widget(self.b2)
        
        self.b3 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b3.bind(on_press = self.sign)
        gl.add_widget(self.b3)
        
        self.b4 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b4.bind(on_press = self.sign)
        gl.add_widget(self.b4)
        
        self.b5 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b5.bind(on_press = self.sign)
        gl.add_widget(self.b5)
        
        self.b6 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b6.bind(on_press = self.sign)
        gl.add_widget(self.b6)
        
        self.b7 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b7.bind(on_press = self.sign)
        gl.add_widget(self.b7)
        
        self.b8 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b8.bind(on_press = self.sign)
        gl.add_widget(self.b8)
        
        self.b9 = Button(text='', background_color = [1,1,1,1], font_size = '50sp', markup = True)
        self.b9.bind(on_press = self.sign)
        gl.add_widget(self.b9)

        self.add_widget(gl)
        self.add_widget(vb)

    def restarter(self, btn):

        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = "Computer"

        self.bb.text = f"{first}" + "'s turn [X]:"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

    def sign(self, btn):
        
        self.count += 1

        if self.P1 == 'X':
            first = self.txt1.text
            second = "Computer"
        else:
            first = "Computer"
            second = self.txt1.text

        if self.count % 2 == 0:
            self.symsign = 'O'
            self.bb.text = first+"'s turn [X]:"
        else:
            self.symsign = 'X'
            self.bb.text = second+"'s turn [O]:"

        btn.text = self.symsign
        if self.check():
            self.winner()
        elif self.count == 9:
            self.draw()

    def texter(self):
        if self.count % 2 == 0:
            return "X"
        else:
            return "O"

    def winreset(self,btn):
        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = "Computer"

        self.bb.text = first+"'s turn [X]:"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

        self.winpop.dismiss()

    def drawreset(self,btn):
        self.count = 0

        if self.P1 == 'X':
            first = self.txt1.text
        else:
            first = "Computer"

        self.bb.text = first+"'s turn [X]:"
        
        self.b1.text = ''
        self.b2.text = ''
        self.b3.text = ''
        self.b4.text = ''
        self.b5.text = ''
        self.b6.text = ''
        self.b7.text = ''
        self.b8.text = ''
        self.b9.text = ''

        self.drawpop.dismiss()

    def winner(self):
        button1 = Button(text = f"{self.symsign} is the winner!\nPress to RESET.")
        button1.bind(on_press = self.winreset)
        self.winpop = Popup(title = 'Result of Game: ', content = button1,  size_hint = (.5, .5))
        self.winpop.open()

    def draw(self):
        button1 = Button(text = f"      Draw!\nPress to RESET.")
        button1.bind(on_press = self.drawreset)
        self.drawpop = Popup(title = 'Result of Game: ', content = button1, size_hint = (.5, .5))
        self.drawpop.open()

    def check(self):

        '''Function to check all the winning conditions.'''
        
        if self.b1.text == self.symsign and self.b2.text == self.symsign and self.b3.text == self.symsign:
            return True
        if self.b4.text == self.symsign and self.b5.text == self.symsign and self.b6.text == self.symsign:
            return True
        if self.b7.text == self.symsign and self.b8.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b1.text == self.symsign and self.b4.text == self.symsign and self.b7.text == self.symsign:
            return True
        if self.b2.text == self.symsign and self.b5.text == self.symsign and self.b8.text == self.symsign:
            return True
        if self.b3.text == self.symsign and self.b6.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b1.text == self.symsign and self.b5.text == self.symsign and self.b9.text == self.symsign:
            return True
        if self.b3.text == self.symsign and self.b5.text == self.symsign and self.b7.text == self.symsign:
            return True

    def assign(self, btn):
        self.t1 = self.txt1.text

        if self.nameChecker():
            symbol = ['X', 'O']
        
            self.P1 = random.choice(symbol)
            if self.P1 == 'X':
                self.P2 = 'O'
            else:
                self.P2 = 'X'

            button1 = Button(text = f"         {self.t1} has {self.P1}.\n         Computer has {self.P2}.\nPress to continue !!!")
            button1.bind(on_press = self.assignp)
            button1.bind(on_press = self.enable)
            self.asspop = Popup(title = 'Symbol Assignment', content = button1, size_hint = (.5, .5))
            self.asspop.open()
        else:
            button2 = Button(text = 'Please enter a valid name.')
            button2.bind(on_press = self.namep)
            self.namepop = Popup(title = 'WARNING!', content = button2, size_hint = (.5,.5))
            self.namepop.open()

    def enable(self, btn):
        self.btn2.disabled = False

    def nameChecker(self):
        flag = False

        if self.txt1.text not in ('', ' '):
            flag = True
        return flag

    def assignp(self,btn):
        self.asspop.dismiss()

    def namep(self,btn):
        self.namepop.dismiss()


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        vb = BoxLayout(orientation='vertical')
        hb = BoxLayout(orientation='horizontal')

        l2 = Label(text = '[b][i][size=95][font=impact]Main Menu[/font][/i][/b][/size]', markup = True)
        vb.add_widget(l2)

        btn1 = Button(text = '[color=#000000][b][i][size=25][font=bahnschrift]Player vs Player', size_hint = (0.5, 0.5), pos_hint = {'x': 0.25}, markup = True, background_normal = 'normal.png', background_down = 'down.png', border = (45,45,45,45))
        btn1.bind(on_press = self.pvp_changer)
        vb.add_widget(btn1)

        l4 = Label(size_hint = (0, .25))
        vb.add_widget(l4)

        btn2 = Button(text = '[color=#000000][b][i][size=25][font=bahnschrift]vs CPU [Easy]', size_hint = (0.5, 0.5), pos_hint = {'x': 0.25}, markup = True, background_normal = 'normal.png', background_down = 'down.png', border = (45,45,45,45))
        btn2.bind(on_press = self.compe_changer)
        vb.add_widget(btn2)

        l5 = Label(size_hint = (0, .25))
        vb.add_widget(l5)

        btn2 = Button(text = '[color=#000000][b][i][size=25][font=bahnschrift]vs CPU [Hard]', size_hint = (0.5, 0.5), pos_hint = {'x': 0.25}, markup = True, background_normal = 'normal.png', background_down = 'down.png', border = (45,45,45,45))
        btn2.bind(on_press = self.comph_changer)
        vb.add_widget(btn2)

        l6 = Label(size_hint = (0, .25))
        vb.add_widget(l6)

        btn2 = Button(text = '[color=#000000][b][i][size=25][font=bahnschrift]Quit', size_hint = (0.5, 0.5), pos_hint = {'x': 0.25}, markup = True, background_normal = 'normal.png', background_down = 'down.png', border = (45,45,45,45))
        btn2.bind(on_press = self.quit_changer)
        vb.add_widget(btn2)

        l7 = Label(size_hint = (0, .25))
        vb.add_widget(l7)

        self.add_widget(vb)


    def pvp_changer(self, *args):
        self.manager.current = 'pvp'

    def compe_changer(self, *args):
        self.manager.current = 'compe'

    def comph_changer(self, *args):
        self.manager.current = 'comph'

    def quit_changer(self, *args):
        self.manager.current = 'welcome'

class TicTacToeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(PvpScreen(name='pvp'))
        sm.add_widget(CompEScreen(name='compe'))
        
        return sm


def main():
    TicTacToeApp().run()


if __name__ == '__main__':
    main()
