from ultralytics import YOLO
from paddleocr import PaddleOCR

class Model:
    def __init__(self):
        self.yolo = YOLO('app/models/best.pt')
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)
    def detect_license_plate(self, frame):
        try:
            results = self.yolo.predict(frame, conf=0.5, verbose=False)
            detections = []
            for result in results:
                if result.boxes:
                    for box in result.boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = box.conf.item()
                        cls = int(box.cls)
                        class_name = result.names[cls]
                        if class_name == 'License_Plate':
                            detections.append((x1, y1, x2, y2, conf, class_name))
            return detections
        except Exception as e:
            print(f'YOLO Detection Failed: {e}')
            return []
    def extract_text_from_plate(self, plate_img):
        try:
            ocr_results = self.ocr.ocr(plate_img, cls=False)
            if ocr_results:
                return ''.join([line[1][0] for line in ocr_results[0]]).strip()
        except Exception as e:
            print(f'OCR Failed: {e}')
        return ""