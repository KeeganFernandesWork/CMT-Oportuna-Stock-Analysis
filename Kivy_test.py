from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
#from kivy.uix.gridlayout import GridLayout

class SayHello(App):
    """Use This to say hello"""

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.button = Button(text = "Get Stocks")
        self.window.add_widget(self.button)

        return self.window


if __name__ == "__main__":
    SayHello().run()
