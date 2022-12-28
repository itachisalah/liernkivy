from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp


class ExmeplStackLayout(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,18):
            x = dp(80)
            b = Button(text=str(i +1),
            size_hint=(None,None),
            size=(x,x))
            self.add_widget(b)
            
            


class salah(App):
    pass


if __name__=='__main__':
    
    salah().run()

