from PySide import QtCore, QtGui
from .ui import teams_ui

from data import champions
from models.team import Team

import supervisor

import os.path
import copy


class TeamsW(QtGui.QWidget, teams_ui.Ui_Form):
    def __init__(self, parent=None):
        super(TeamsW, self).__init__(parent)

        self.ui = teams_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.edit_field = [self.ui.name, self.ui.tag, self.ui.top,
                              self.ui.jungle, self.ui.mid, self.ui.adc,
                              self.ui.support]

        self.updating = False
        self.team = Team()
        self.connect_actions()

    def connect_actions(self):
        self.ui.load_button.pressed.connect(self.load_team)
        self.ui.save_button.pressed.connect(self.save_team)

        for edit in self.ui.edit_field:
            edit.textChanged.connect(self.button_state)
            edit.textChanged.connect(self.update_team)

        self.ui.set_blue_button.pressed.connect(self.set_blue_team)
        self.ui.set_purple_button.pressed.connect(self.set_purple_team)

        self.ui.clear_button.pressed.connect(self.clear_fields)

    def set_purple_team(self):
        supervisor.Supervisor.match().set_purple_team(copy.deepcopy(self.team))

    def set_blue_team(self):
        supervisor.Supervisor.match().set_blue_team(copy.deepcopy(self.team))

    def button_state(self):
        # Check tag field
        if self.ui.tag != '':
            # Check if file exists
            if os.path.isfile(u'./teams/' + self.ui.tag.text() + '.json'):
                self.ui.load_button.setEnabled(True)
            else:
                self.ui.load_button.setEnabled(False)

            self.ui.save_button.setEnabled(True)
        else:
            self.ui.save_button.setEnabled(False)
            self.ui.load_button.setEnabled(False)

    def load_team(self):
        self.team.load_json()
        self.update_fields()

    def save_team(self):
        self.update_team()
        self.team.save_json()

    def update_team(self):
        if self.updating:
            return
        self.team.populate(self.ui.name.text(), self.ui.tag.text(),
                           self.ui.top.text(), self.ui.jungle.text(),
                           self.ui.mid.text(), self.ui.adc.text(),
                           self.ui.support.text())

    def update_fields(self):
        self.updating = True
        self.ui.name.setText(self.team.name)
        self.ui.tag.setText(self.team.tag)
        self.ui.top.setText(self.team.top)
        self.ui.jungle.setText(self.team.jungle)
        self.ui.mid.setText(self.team.mid)
        self.ui.adc.setText(self.team.adc)
        self.ui.support.setText(self.team.support)
        self.updating = False

    def clear_fields(self):
        self.updating = True
        self.ui.name.setText('')
        self.ui.tag.setText('')
        self.ui.top.setText('')
        self.ui.jungle.setText('')
        self.ui.mid.setText('')
        self.ui.adc.setText('')
        self.ui.support.setText('')
        self.updating = False
