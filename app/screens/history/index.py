from kivy.uix.screenmanager import Screen
import csv
from kivy.lang import Builder

Builder.load_file('app/ui/history/index.kv')

class HistoryIndex(Screen):
    def on_enter(self):
        self.load_history()

    def load_history(self):
        try:
            with open('app/data/data.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = [row['plat_nomor'] for row in reader]  # Extract the plate numbers

            # Update the RecycleView data
            self.ids.history_list.data = [{'text': f"{i + 1}. {plate}"} for i, plate in enumerate(data)]
        except FileNotFoundError:
            # If the file doesn't exist, show a placeholder message
            self.ids.history_list.data = [{'text': "No history available."}]
