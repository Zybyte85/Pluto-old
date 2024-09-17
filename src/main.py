from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
import os
import datetime
import json
from functions import *

# Set some variables
theme_path = 'themes/default-dark/'

theme_json = json.load(open(theme_path + 'theme.json', 'r'))

id_file_path = 'data/id_file.txt'


class Application:
    def __init__(self, ui_file):
        '''
        Constructor for the Application class.

        Sets the Qt::AA_ShareOpenGLContexts attribute, creates an instance of QApplication,
        loads the specified ui file, sets some properties, and loads some icons.

        :param ui_file: The path to the ui file to load.
        '''
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

        # Create an instance of QApplication
        self.app = QApplication([])

        # Create a loader object
        loader = QUiLoader()

        # Load the ui file
        try:
            self.ui = loader.load(ui_file)
            print(f'Loaded {ui_file}')
        except FileNotFoundError:
            print(f'File not found: {ui_file}')

        # Set some properties and load some icons
        self.ui.settingsButton.setIcon(
            QIcon(theme_path + 'icons/settings.png')
        )
        self.ui.settingsButton.setIconSize(QSize(38, 38))
        self.ui.calendarButton.setIcon(
            QIcon(theme_path + 'icons/calendar.png')
        )
        self.ui.calendarButton.setIconSize(QSize(32, 32))
        self.ui.newButton.clicked.connect(self.handle_new_button_click)
        self.ui.show()

    def make_task(self, priority, text, due_date, due_time, initial=False):
        '''
        Creates a new task button and adds it to the corresponding layout.

        If initial is False, it also writes the task to the json file and increments the id number.

        :param priority: The priority of the task. Can be 'high', 'medium', or 'low'.
        :param text: The text to show on the button.
        :param due_date: The due date of the task.
        :param due_time: The due time of the task.
        :param initial: Whether or not this is an initial task created when the program starts.
        '''
        priority = priority.split()[0].lower()

        task = QPushButton(text)

        task.clicked.connect(lambda checked: handle_button_click(task))
        print(task.text())
        if not initial:
            id_file = int(
                open('data/id_file.txt', 'r').read()
            )  # Read the current value
            write_json(
                {
                    'text': text,
                    'due_date': due_date,
                    'due_time': due_time,
                    'id': id_file,
                },
                priority,
            )
            id_file += 1  # Increment the value
            open('data/id_file.txt', 'w').write(
                str(id_file)
            )  # Write the updated value back to the file

        if priority == 'high':
            task.setStyleSheet(theme_json['style'][0]['high_priority'])
            self.ui.HighPriorityLayout.addWidget(task)
        elif priority == 'medium':
            task.setStyleSheet(theme_json['style'][0]['medium_priority'])
            self.ui.MediumPriorityLayout.addWidget(task)
        elif priority == 'low':
            self.ui.LowPriorityLayout.addWidget(task)
            task.setStyleSheet(theme_json['style'][0]['low_priority'])

    def handle_new_button_click(self):
        '''
        Handle the new button being clicked.

        This is a slot for the newButton's clicked signal. It creates a new
        Dialog and creates a new task with default values.s

        :return: None
        '''

        print('New button clicked!')
        self.dialog = Dialog(self)
        if self.dialog.ui.exec() == 0:
            print('Make task canceled')
        else:
            print('Accepted make task')
            self.make_task(
                self.dialog.ui.taskPriority.currentText(),
                self.dialog.ui.taskName.toPlainText(),
                self.dialog.ui.taskTime.time().toString(),
                self.dialog.ui.taskDate.date().toString(),
            )



class Dialog:
    def __init__(self, app):
        '''
        Constructor for the Dialog class.

        :param app: The application instance.
        '''
        self.app = app
        self.loader = QUiLoader()
        self.ui = self.loader.load('assets/new_task.ui')
        self.ui.show()


if __name__ == '__main__':
    app = Application('assets/day_view.ui')
    app.ui.setStyleSheet(theme_json['style'][0]['main_window'])
    load_tasks_from_dict(Application, app, load_json())

    # Start the application's event loop
    app.app.exec()
