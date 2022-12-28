from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


class G(GridLayout):
    menu= StringProperty('0')
    num = 0
    def click_btn(self):
        self.num+=1
        self.menu = f'{self.num}'


class main(App):
    pass
    
main().run()