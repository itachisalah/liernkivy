from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Ellipse
from kivy.properties import Clock


class exm(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.t = dp(50)
        self.vx= dp(9)
        self.vy= dp(4)
        
        
        
        with self.canvas:
            self.ball=Ellipse(pos=(100,100),size=(self.t,self.t))
            
            Clock.schedule_interval(self.update,1/60)
    
    def on_size(self,*args):
        self.ball.pos=(self.center_x-self.t/2,self.center_y-self.t/2)
        
        
    def update(self,dt):
        x,y= self.ball.pos
        
        t_x ,t_y = self.ball.size
        
        l , a = self.width,self.height
        
        if y + t_y > self.height:
            self.vy *=-1
        if y <=0:
            self.vy *= -1
             
        if x + t_x > self.width:
            self.vx *=-1
        if x<=0:
            self.vx *=-1  
             
        y += self.vy
        x +=self.vx
        
        
        
        self.ball.pos=(x,y)


class Main(App):
    pass
    
    
Main().run()