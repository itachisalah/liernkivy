from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class G(GridLayout):
    num_text=StringProperty('0')
    num=0
    def click_num(self):
        self.num +=1
        self.num_text=f'{self.num}'
      
    def toggle(self, widget):
        if widget.state== 'normal':
            widget.text='OFF'
        else:
            widget.text='ON'

class Main(App):
    pass
    
Main().run()