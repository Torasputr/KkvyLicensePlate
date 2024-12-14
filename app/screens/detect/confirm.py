from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import csv
import os

Builder.load_file('app/ui/detect/confirm.kv')

class DetectConfirm(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def set_plate_text(self, text):
        self.ids.plate_input.text = text
    def save_plate_to_csv(self, plate_text):
        file_path = 'app/data/data.csv'
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['plat_nomor'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'plat_nomor': plate_text})
        print(f"Plate '{plate_text}' successfully saved to {file_path}")

    def confirm_plate(self):
        confirmed_text = self.ids.plate_input.text.strip()
        if confirmed_text:
            self.save_plate_to_csv(confirmed_text)
        self.manager.current = 'detectSuccess'
    def go_back(self):
        self.manager.current = 'detectIndex'