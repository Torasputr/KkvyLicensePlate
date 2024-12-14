from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.screens.home.index import HomeIndex
from app.screens.detect.index import DetectIndex
from app.screens.detect.confirm import DetectConfirm
from app.screens.detect.success import DetectSuccess
from app.screens.history.index import HistoryIndex

class LicensePlateApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeIndex(name='homeIndex'))
        sm.add_widget(DetectIndex(name='detectIndex'))
        sm.add_widget(DetectConfirm(name='detectConfirm'))
        sm.add_widget(DetectSuccess(name='detectSuccess'))
        sm.add_widget(HistoryIndex(name='historyIndex'))
        return sm

if __name__ == '__main__':
    LicensePlateApp().run()