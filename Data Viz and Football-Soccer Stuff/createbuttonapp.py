from kivy.app import App
from kivy.uix.button import Button

class CreateButtonApp(App):
    # Main class instantiated for running application
    def build(self):
        '''
        Objective: To initialize application with widget tree
        Input Parameters:
            self (implicit parameter) - object of type
            CreateButtonApp
        Return Value: instance of Button class (root widget)
        '''
        return Button(text = 'Hello')


if __name__ == '__main__':
    CreateButtonApp().run()
