import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)

        self.createMenuBar()

        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Menu System Example')

    def createMenuBar(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        fileMenu = QMenu('File', self)
        menubar.addMenu(fileMenu)

        newAction = QAction('New', self)
        newAction.triggered.connect(self.onNew)
        fileMenu.addAction(newAction)

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.onQuit)
        fileMenu.addAction(quitAction)

        settingsMenu = QMenu('Settings', self)
        menubar.addMenu(settingsMenu)

        preferencesAction = QAction('Preferences', self)
        preferencesAction.triggered.connect(self.onPreferences)
        settingsMenu.addAction(preferencesAction)

    def onNew(self):
        print('New action triggered')

    def onQuit(self):
        QApplication.quit()

    def onPreferences(self):
        # Change the menu items dynamically
        fileMenu = self.menuBar().findChild(QMenu, 'File')
        fileMenu.clear()

        newAction = QAction('New', self)
        newAction.triggered.connect(self.onNew)
        fileMenu.addAction(newAction)

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.onQuit)
        fileMenu.addAction(quitAction)

        settingsMenu = self.menuBar().findChild(QMenu, 'Settings')
        settingsMenu.clear()

        preferencesAction = QAction('New Preferences', self)
        preferencesAction.triggered.connect(self.onNewPreferences)
        settingsMenu.addAction(preferencesAction)

    def onNewPreferences(self):
        print('New Preferences action triggered')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())