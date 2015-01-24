from PySide import QtCore, QtGui
from .ui import menu_ui

from .livew import LiveW
from .teamsw import TeamsW
from .lineupw import LineupW


class MainW(QtGui.QMainWindow, menu_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainW, self).__init__(parent)

        # Main window
        self.ui = menu_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_actions()

        # Other window
        self.live = LiveW()
        self.teams = TeamsW()
        self.lineup = LineupW()

    def toggle(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    def connect_actions(self):
        self.ui.exit_button.clicked.connect(self.quitApp)
        self.ui.live_button.clicked.connect(lambda: self.toggle(self.live))
        self.ui.team_button.clicked.connect(lambda: self.toggle(self.teams))
        self.ui.lineup_button.clicked.connect(lambda: self.toggle(self.lineup))


    def quitApp(self):
        QtGui.QApplication.quit()

    def main(self):
        '''Main code to start the setting up of the application'''
        # Showing the main window
        self.show()
