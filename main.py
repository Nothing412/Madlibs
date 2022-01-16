from ursina import *
import os
from ursina.color import white

class quit2(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'quad',
            color = color.black,
            position = (0,-1.2,1),
            text = "Quit",
            scale = (3,1,1)
            )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
               quit()
               
               
               
               
class play(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "quad",
            text = "Play",
            scale = (3,1,1),
            color = color.black,
            
            )
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                
                os.system("game.py")
                os.system("game.pyc")
                quit()
                
                

app =Ursina(borderless = False, title ="Mad libs")
def play_button_on_click():
    play_button.color =color.black

window.fps_counter.enabled = False
window.color = color.white
play_button = play()
quit_button = quit2()


app.run()