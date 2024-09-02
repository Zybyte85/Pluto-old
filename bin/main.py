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

        if not initial:
            write_json({"text": text, "description": description, "due_date": due_date}, priority)

        #button.clicked.connect(self.handle_button_click)
        if priority == "high":
            task.setStyleSheet('background-color: #20e361;' + stylesheet_extras)
            self.ui.HighPriorityLayout.addWidget(task)
        elif priority == "medium":
            task.setStyleSheet('background-color: #ffe600;'  + stylesheet_extras)
            self.ui.MediumPriorityLayout.addWidget(task)
        elif priority == "low":
            self.ui.LowPriorityLayout.addWidget(task)
            task.setStyleSheet('background-color: #e86541;' + stylesheet_extras)

        # Instantiate buttons
        #for i in range(10):
        #    now = datetime.datetime.now()
        #    app.make_task(app, "high", "Task " + str(i + 1), "Description", now.timestamp())
        #    app.make_task(app, "medium", "Task " + str(i + 1), "Description", now.timestamp())
        #    app.make_task(app, "low", "Task " + str(i + 1), "Description", now.timestamp())

if __name__ == "__main__":
    app = Application(os.path.join(app_path, "assets/day_view.ui"))
    load_tasks_from_dict(load_json())

    # Start the application's event loop
    app.app.exec()