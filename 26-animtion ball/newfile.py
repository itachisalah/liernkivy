from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Ellipse
from kivy.properties import Clock


class exm(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.t = dp(50)
        
        with self.canvas:
            self.ball=Ellipse(pos=(100,100),size=(self.t,self.t))
            
            Clock.schedule_interval(self.update,1/60)
    
    def on_size(self,*args):
        self.ball.pos=(self.center_x-self.t/2,self.center_y-self.t/2)
        
        
    def update(self,dt):
        x,y= self.ball.pos
        self.ball.pos=(x+4,y)


class Main(App):
    pass
    
    
Main().run()