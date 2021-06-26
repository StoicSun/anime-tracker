import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialise infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set colms 
        self.cols = 2

        # Add widgets 
        self.add_widget(Label(text="Name: "))
        # Add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Password box
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        # Login button
        self.login = Button(text="Login", font_size=32)
        # Bind the button
        self.login.bind(on_press=self.press)
        self.add_widget(self.login)

    # Doing something with the usr input
    def press(self, instance):
        name = self.name.text
        password  = self.password.text
        # logging attempts at login
        if password == 'password':
            print(f'{name},{password}') 
            self.add_widget(Label(text="Login successfull"))

        # Clearing the text boxes 
        self.name.text = ''
        self.password.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__  == '__main__':
    MyApp().run()