import cv2
from kivy.graphics.texture import Texture
from app.utils.model import Model

class Camera:
    def __init__(self):
        self.cap = None
        self.model = Model()
    def initialize(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise Exception('Camera Failed to Initialize')
    def read_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                return frame
        return None
    def process_frame(self, frame):
        detections = self.model.detect_license_plate(frame)
        annotated_frame = frame.copy()
        detected_texts = []
        for x1, y1, x2, y2, conf, class_name in detections:
            license_plate_img = frame[y1:y2, x1:x2]
            plate_text = self.model.extract_text_from_plate(license_plate_img)
            detected_texts.append(plate_text)
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_frame, plate_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(f'The Confidence of the Detection is: {conf}')
        return annotated_frame, detected_texts
    def release(self):
        if self.cap:
            self.cap.release()
            self.cap = None
    def frame_to_texture(self, frame):
        if frame is not None:
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buffer, colorfmt='rgb', bufferfmt='ubyte')
            return texture
        return None 