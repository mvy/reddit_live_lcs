from PySide import QtCore, QtGui
from .ui import lineup_ui
from data import champions
from models.match import Lineup

import supervisor


class LineupW(QtGui.QWidget, lineup_ui.Ui_Form):
    def __init__(self, parent=None):
        super(LineupW, self).__init__(parent)

        self.ui = lineup_ui.Ui_Form()
        self.ui.setupUi(self)

        self.combos_blue = [self.ui.blue_top,
                            self.ui.blue_jungle, self.ui.blue_mid,
                            self.ui.blue_adc, self.ui.blue_support]
        self.combos_purple = [self.ui.purple_top, self.ui.purple_jungle,
                              self.ui.purple_mid, self.ui.purple_adc,
                              self.ui.purple_support]
        self.populate_combos()
        self.connect_actions()

    def connect_actions(self):
        self.ui.set_button.pressed.connect(self.set_lineup)

    def populate_combos(self):
        for combo in self.combos_blue + self.combos_purple:
            combo.addItems(champions.champion_list)

    def set_lineup(self):
        lineup_ = Lineup()

        lineup_.set_blue_top(self.ui.blue_top.currentText())
        lineup_.set_blue_jungle(self.ui.blue_jungle.currentText())
        lineup_.set_blue_mid(self.ui.blue_mid.currentText())
        lineup_.set_blue_adc(self.ui.blue_adc.currentText())
        lineup_.set_blue_support(self.ui.blue_support.currentText())

        lineup_.set_purple_top(self.ui.purple_top.currentText())
        lineup_.set_purple_jungle(self.ui.purple_jungle.currentText())
        lineup_.set_purple_mid(self.ui.purple_mid.currentText())
        lineup_.set_purple_adc(self.ui.purple_adc.currentText())
        lineup_.set_purple_support(self.ui.purple_support.currentText())

        supervisor.Supervisor.match().set_lineup(lineup_)
