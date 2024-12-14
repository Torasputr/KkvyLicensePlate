from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from app.utils.camera import Camera
from kivy.clock import Clock
# from app.utils.model import Model

Builder.load_file('app/ui/detect/index.kv')

class DetectIndex(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = Camera()
        self.capture_event = None
        self.detected_text = None
    def update_feed(self, dt):
        frame = self.camera.read_frame()
        if frame is not None:
            annotated_frame, detected_texts = self.camera.process_frame(frame)
            texture = self.camera.frame_to_texture(annotated_frame)
            self.ids.camera_feed.texture = texture

            if detected_texts:
                self.ids.ocr_result.text = f"Detected Plate: {', '.join(detected_texts)}"
                self.detected_text = detected_texts[0]
            else:
                self.ids.ocr_result.text = "Detected Plate: None"
                self.detected_text = None
    def on_enter(self):
        try:
            self.camera.initialize()
            self.update_event = Clock.schedule_interval(self.update_feed, 1/30)
        except Exception as e:
            print(f'Error while starting camera: {e}')
    def on_leave(self):
        if self.update_event:
            Clock.unschedule(self.update_event)
            self.update_event = None
        self.camera.release()
    def go_back(self):
        self.on_leave()
        self.manager.current = 'homeIndex'
    def go_confirm(self):
        if self.detected_text:
            self.on_leave()
            confirm_screen = self.manager.get_screen('detectConfirm')
            confirm_screen.set_plate_text(self.detected_text)
            self.manager.current = 'detectConfirm'
        else:
            self.ids.ocr_result.text = "No plate detected. Please try again."
            Clock.schedule_once(self.reset_ocr_result, 2)