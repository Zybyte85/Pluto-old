from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
import os
import datetime
import json

app_path = os.path.dirname(os.path.dirname(__file__))

def handle_button_click():
        print("Button clicked!")

def load_json(filename='data/tasks.json'):
    with open(os.path.join(app_path, filename), "r") as file:
        return json.load(file)

def write_json(new_data, priority, filename='data/tasks.json'):
    with open(os.path.join(app_path, filename), "r+") as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[priority].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

class Application:
    def __init__(self, ui_file):
        # Set the Qt::AA_ShareOpenGLContexts attribute
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

        # Create an instance of QApplication
        self.app = QApplication([])

        # Create a loader object
        loader = QUiLoader()

        # Load the ui file
        try:
            self.ui = loader.load(ui_file)
            print(f"Loaded {ui_file}")
        except FileNotFoundError:
            print(f"File not found: {ui_file}")

        self.ui.settingsButton.setIcon(QIcon(os.path.join(app_path, "assets/SettingsGear.png")))
        self.ui.settingsButton.setIconSize(QSize(38, 38))
        self.ui.calendarButton.setIcon(QIcon(os.path.join(app_path, "assets/CalendarIcon.png")))
        self.ui.calendarButton.setIconSize(QSize(32, 32))

        #self.ui.newButton.connect(handle_button_click())

        self.ui.show()
        
    def make_task(self, priority, text, description, due_date, initial=False):
        task = QPushButton(text)

        if not initial:
            write_json({"text": text, "description": description, "due_date": due_date}, priority)

        #button.clicked.connect(self.handle_button_click)
        if priority == "high":
            task.setStyleSheet('background-color: rgb(51, 209, 122); color: rgb(0, 0, 0);')
            self.ui.HighPriorityLayout.addWidget(task)
        elif priority == "medium":
            task.setStyleSheet('background-color: rgb(248, 228, 92);color: rgb(0, 0, 0);')
            self.ui.MediumPriorityLayout.addWidget(task)
        elif priority == "low":
            self.ui.LowPriorityLayout.addWidget(task)
            task.setStyleSheet('background-color: rgb(255, 120, 0);color: rgb(0, 0, 0);')

        # Instantiate buttons
        #for i in range(10):
        #    now = datetime.datetime.now()
        #    app.make_task(app, "high", "Task " + str(i + 1), "Description", now.timestamp())
        #    app.make_task(app, "medium", "Task " + str(i + 1), "Description", now.timestamp())
        #    app.make_task(app, "low", "Task " + str(i + 1), "Description", now.timestamp())

def load_tasks_from_dict(data):
    for y in data.keys():
        for i in range(data[y].__len__()):
            Application.make_task(app, y, data[y][i]["text"], data[y][i]["description"], data[y][i]["due_date"], True)

if __name__ == "__main__":
    app = Application(os.path.join(app_path, "assets/day_view.ui"))
    load_tasks_from_dict(load_json())

    # Start the application's event loop
    app.app.exec()