from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

#Cepi Ramdhani
class Layar1(Screen):
    pass

class Demo1(Screen):
    pass

class Demo2(Screen):
    pass

class Demo3(Screen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
       
        sm = ScreenManager()
        sm.add_widget(Layar1(name = "layar1"))
        sm.add_widget(Demo1(name = "demo1"))
        sm.add_widget(Demo2(name = "demo2"))
        sm.add_widget(Demo3(name = "demo3"))

        return sm

Main().run()