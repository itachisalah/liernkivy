from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class Botn(GridLayout):
    menu = StringProperty('salaheddine')
    
    def click(self):
        self.menu = 'iatchi'


class mainApp(App):
    pass
    
mainApp().run()