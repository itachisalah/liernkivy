from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


class WidgetPrincipal(Widget):
    ponto_x=NumericProperty(0)
    ponto_y=NumericProperty(0)
    
    NUM_LINHAS_V= 7
    ESPACO_LINHAS_V=0.1
    
    linhas_verticais=[]
    
    def __init__(self,**kwargs):
        super(WidgetPrincipal,self).__init__(**kwargs)
        self.init_linhas_verticais()
        
    def on_parent(self,widget,parent):
        pass
        
    def  on_size(self,*args):
        pass
        
    def on_ponto_x(self,widget,valor):
        pass
        
           
    def on_ponto_y(self,widget,valor):
        pass   
    
    def init_linhas_verticais(self):
        with self.canvas:
            Color(1,1,1)   
            for i in range(0,self.NUM_LINHAS_V):
                self.linhas_verticais.append(Line())



    def atulizer_linhas_vertcais(self):
        linha_central_x = int(self.width/2)
        espac= self.ESPACO_LINHAS_V*self.width
        offset = -int(self.NUM_LINHAS_V /2)
        
        for i in range(0,self.NUM_LINHAS_V):
            linha_x =int(linha_central_x + offset * espac)
            self.linhas_vertcais[i].points=[linha_x,0,linha_x,self.height]
            
            offset +=1

class Galaxy(App):
    def build(self):
        pass
        
        
if __name__=='__main__':
    Galaxy().run()