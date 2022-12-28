from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line , Rectangle
from kivy.graphics.context_instructions import Color




class itachi(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        with self.canvas:
            Color(1,0,0)
            Line(points=(500,1000,700,1400),width=4)
            Color(0,1,0)
            Line(circle=(500,200,80),width=2)
            Line(rectangle=(500,400,100,100),width=3)
            Color(0,0,1)
            Rectangle(pos=(500,600),
            size=(300,100))



class salah(App):
    pass
    
    
salah().run()