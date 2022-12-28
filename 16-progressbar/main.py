from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty

class G(GridLayout):
    num_text=StringProperty('0')
    num=0
    num_active =BooleanProperty(False)
    
    def click_num(self):
        if self.num_active:
            self.num +=1
            self.num_text=f'{self.num}'
      
    def toggle(self, widget):
        if widget.state== 'normal':
            widget.text='OFF'
            self.num_active=False
        else:
            widget.text='ON'
            self.num_active=True
    

class Main(App):
    pass
    
Main().run()