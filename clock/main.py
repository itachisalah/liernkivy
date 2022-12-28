from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty,NumericProperty
from datetime import datetime
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock





class ImageButton(ButtonBehavior, Image):
    pass

class ClockApp(BoxLayout):
    current_time= StringProperty(str(datetime.now().strftime('%H:%M')))
    
    seconds_on = False
    day_and_month_on= False
    day_of_week_on=False
    year_on=False
    
    date_label = Label(pos=(0,dp(-60)))
    
    stopwatch_time=NumericProperty(0)
    
    def __init__(self,**kwargs):
        super(ClockApp,self).__init__(**kwargs)
        
        Clock.schedule_interval(self.update_time,0.5)
        self.ids.clock_screen_id.add_widget(self.date_label)
        
    def update_time(self,*args):
       
        self.current_time=str(datetime.now().strftime('%H:%M'+(':%S' if self.seconds_on else '')))
        
    def update_screen(self,insrance,switch_value,option):
        if option =='seconds':
            self.seconds_on =switch_value
        if option =='day_+_month':
            self.day_and_month_on = switch_value
        if option== 'day_of_week':
            self.day_of_week_on  = switch_value
        if option == 'year':
            self.year_on =switch_value
        
        self.date_label.text=datetime.now().strftime(('%a' if self.day_of_week_on else '')
    +('%d%b'
if self.day_and_month_on else '')
+('%Y' if self.year_on else '')).strip()


    def start_stopwatch(self,instance):
        Clock.schedule_interval(self.update_stopwatch,0.1)
        self.ids.start_button.disabled=True
        self.ids.stop_button.disabled=False
        
    
    def stop_stopwatch(self,instance):
        Clock.unschedule(self.update_stopwatch)
        self.ids.start_button.disabled=False
        self.ids.stop_button.disabled=True
     
    def reset_stopwatch(self,instance):
              self.stop_stopwatch =0        
              
        
    def update_stopwatch(self,*args):
        self.stopwatch_time+=0.1
        
        self.stopwatch_time =float('%.1f'%(self.stopwatch_time))
    

class Main(App):
    def build(self):
        return ClockApp()
        
if __name__=='__main__':
    Main().run()