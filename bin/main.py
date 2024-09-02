from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
import os
import datetime
import json
from functions import *

stylesheet_extras = 'color: rgb(0, 0, 0); border: none; border-radius: 4px; padding:4px 4px;'

app_path = os.path.dirname(os.path.dirname(__file__))

id_file_path = "data/id_file.txt"

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
        self.ui.newButton.clicked.connect(self.handle_new_button_click)
        self.ui.show()

        
    def make_task(self, priority, text, description, due_date, initial=False):
        task = QPushButton(text)

        task.clicked.connect(lambda checked: handle_button_click(task))

        if not initial:
            id_file = int(open("data/id_file.txt", 'r').read())  # Read the current value
            write_json({"text": text, "description": description, "due_date": due_date, "id": id_file}, priority)
            id_file += 1  # Increment the value
            open("data/id_file.txt", 'w').write(str(id_file))  # Write the updated value back to the file


        if priority == "high":
            task.setStyleSheet('background-color: #20e361;' + stylesheet_extras)
            self.ui.HighPriorityLayout.addWidget(task)
        elif priority == "medium":
            task.setStyleSheet('background-color: #ffe600;'  + stylesheet_extras)
            self.ui.MediumPriorityLayout.addWidget(task)
        elif priority == "low":
            self.ui.LowPriorityLayout.addWidget(task)
            task.setStyleSheet('background-color: #e86541;' + stylesheet_extras)

    def handle_new_button_click(self):
        print("New button clicked!")
        self.make_task("high", "Task", "Description", "Due Date")

if __name__ == "__main__":
    app = Application(os.path.join(app_path, "assets/day_view.ui"))
    load_tasks_from_dict(Application, app, load_json())

    # Start the application's event loop
    app.app.exec()