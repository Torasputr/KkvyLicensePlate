from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('app/ui/home/index.kv')

class HomeIndex(Screen):
    def __init__(self, **kwargs):
        super(HomeIndex, self).__init__(**kwargs)
    def navigate_to_detect(self):
        self.manager.current = "detectIndex"
    def navigate_to_history(self):
        self.manager.current = "historyIndex"