from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file('app/ui/detect/success.kv')

class DetectSuccess(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self):
        Clock.schedule_once(self.go_to_home_wait, 3)
    def go_to_home_wait(self, dt):
        self.manager.current = 'homeIndex'
    def go_to_home(self):
        self.manager.current = 'homeIndex'