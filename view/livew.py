from PySide import QtCore, QtGui
from view.ui import live_ui
from data import formats
from models import formatter

import supervisor
import re
import pyperclip

split_lambda = lambda name: name.split('_')
position_lambda = lambda name: split_lambda(name)[-1]
action_lambda = lambda name: split_lambda(name)[1]
colour_lambda = lambda name: split_lambda(name)[0]

class LiveW(QtGui.QWidget, live_ui.Ui_Form):
    """Live view form

    Displays the elements to create a game sequence and get the corresponding
    reddit-formatted string"""

    sequenceChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(LiveW, self).__init__(parent)

        self.ui = live_ui.Ui_Form()
        self.ui.setupUi(self)

        self.ui.blue_buttons = [self.ui.blue_top, self.ui.blue_jungle,
                                self.ui.blue_mid, self.ui.blue_adc,
                                self.ui.blue_support]

        self.ui.purple_buttons = [self.ui.purple_top, self.ui.purple_jungle,
                                  self.ui.purple_mid, self.ui.purple_adc,
                                  self.ui.purple_support]

        self.ui.action_buttons = [self.ui.action_none_button,
                                  self.ui.action_kill_button]

        self.sequence = []

        self.connect_actions()

        self.match_ = supervisor.Supervisor.match()
        #self.init_machine()

    def init_machine(self):
        self.state_machine = QtCore.QStateMachine()

        # List of states
        cleared = QtCore.QState()
        blue = QtCore.QState()
        purple = QtCore.QState()
        action = QtCore.QState()
        blue_action = QtCore.QState()
        purple_action = QtCore.QState()
        blue_action_on_purple = QtCore.QState()
        purple_action_on_blue = QtCore.QState()

        # Transitions

        # Initial state

        # Staro

    def uncheck_all(self):
        """Unchecks all buttons"""
        for b_ in (self.ui.blue_buttons + self.ui.purple_buttons +
                   self.ui.action_buttons):
            b_.setChecked(False)

    def connect_actions(self):
        """Connects the UI elements to the functions"""
        supervisor.Supervisor.match().teamHasChanged.connect(self.update_teams)
        supervisor.Supervisor.match().lineupHasChanged.connect(
            self.update_lineup)

        # Connect blue buttons
        for bb_ in self.ui.blue_buttons:
            bb_.clicked.connect(self.on_blue_button_clicked)

        # Connect purple buttons
        for pb_ in self.ui.purple_buttons:
            pb_.clicked.connect(self.on_purple_button_clicked)

        # Connect action buttons
        for ab_ in self.ui.action_buttons:
            ab_.clicked.connect(self.on_action_button_clicked)

        # Connect sequence changed
        self.sequenceChanged.connect(self.on_sequence_changed)

    def on_sequence_changed(self):
        if len(self.sequence) == 3:
            action_ = action_lambda(self.sequence[0].objectName())

            actor_colour_ = colour_lambda(self.sequence[1].objectName())
            actee_colour_ = colour_lambda(self.sequence[2].objectName())
            actor_position_ = position_lambda(self.sequence[1].objectName())
            actee_position_ = position_lambda(self.sequence[2].objectName())

            actor_team_ = getattr(self.match_, actor_colour_ + "_team")()
            actor_champion_ = getattr(self.match_.lineup(),
                                      actor_colour_ + "_" + actor_position_)

            actee_team_ = getattr(self.match_, actee_colour_ + "_team")()
            actee_champion_ = getattr(self.match_.lineup(),
                                      actee_colour_ + "_" + actee_position_)

            actor_ = getattr(actor_team_, actor_position_)
            actee_ = getattr(actee_team_, actee_position_)

            if action_ == "kill":
                clip_ = formatter.Formatter.format_kill(actor_, actor_team_.tag,
                                                        actor_position_,
                                                        actor_champion_, actee_,
                                                        actee_team_.tag,
                                                        actee_position_,
                                                        actee_champion_)
                pyperclip.copy(clip_)

                # Restart for kill action
                self.sequence = self.sequence[:2]
                self.uncheck_players()



    def on_action_button_clicked(self):
        self.uncheck_players()

        if self.sender().objectName() != 'action_none_button':
            self.sequence = [self.sender()]

        # Uncheck other actions
        for b_ in [button_ for button_ in self.ui.action_buttons if button_ !=
                   self.sender()]:
            b_.setChecked(False)

    def on_player_clicked(self):
        """When a purple button is clicked:
        - Unchecked other purple buttons when one is clicked
        - Add it to the action sequence"""
        colour_ = colour_lambda(self.sender().objectName())
        buttons_ = getattr(self.ui, colour_ + "_buttons")

        # TODO: use the second list and map setChecked ?
        for b_ in [button_ for button_ in buttons_ if button_ != self.sender()]:
            b_.setChecked(False)

        # Remove any colour button from the sequence
        self.sequence = [seq_ for seq_ in buttons_ if button_ != self.sender()]

        position_ = position_lambda(self.sender().objectName())

        self.clip_player(colour_, position_)

        # Manage sequence
        self.sequence.append(self.sender())
        self.sequenceChanged.emiot()


    def on_blue_button_clicked(self):
        """When a blue button is clicked:
        - Unchecked other blue buttons when one is clicked
        - Add it to the action sequence"""
        for b_ in [button_ for button_ in self.ui.blue_buttons if button_ !=
                   self.sender()]:
            b_.setChecked(False)

        # Remove any blue button from the sequence
        self.sequence = [seq_ for seq_ in self.sequence if seq_ not in
                         self.ui.blue_buttons]

        # Copy to clipboard
        oname_ = self.sender().objectName()
        position_ = position_lambda(oname_)

        self.clip_player("blue", position_)

        # Manage sequence
        self.sequence.append(self.sender())
        self.sequenceChanged.emit()

    def on_purple_button_clicked(self):
        """When a purple button is clicked:
        - Unchecked other purple buttons when one is clicked
        - Add it to the action sequence"""
        for b_ in [button_ for button_ in self.ui.purple_buttons if button_ !=
                   self.sender()]:
            b_.setChecked(False)

        # Remove any purple button from the sequence
        self.sequence = [seq_ for seq_ in self.sequence if seq_ not in
                         self.ui.purple_buttons]

        # Copy to clipboard
        oname_ = self.sender().objectName()
        position_ = position_lambda(oname_)

        self.clip_player("purple", position_)

        # Manage sequence
        self.sequence.append(self.sender())
        self.sequenceChanged.emit()

    def clip_player(self, colour, position_):
        player_ = getattr(getattr(self.match_, colour + '_team')(), position_)
        champion_ = getattr(self.match_.lineup(), colour + '_' + position_)
        team_ = formats.team.format(
            team=getattr(
                    getattr(self.match_, colour + "_team")(),
                    "name"))

        clip_ = formats.player.format(name=player_, champion=champion_,
                                    position=position_, team=team_)

        pyperclip.copy(clip_)

    def update_teams(self):
        """Updates the button with the team players' names (from match)"""
        bplayers_ = self.match_.list_blue_players()
        pplayers_ = self.match_.list_purple_players()

        if bplayers_:
            self.set_blue_team(bplayers_)

        if pplayers_:
            self.set_purple_team(pplayers_)

    def update_lineup(self):
        """Updates the buttons with the lineup (from match)"""
        bchampions_ = self.match_.lineup().list_blue_champions()
        pchampions_ = self.match_.lineup().list_purple_champions()

        if bchampions_:
            self.set_blue_champion(bchampions_)
        if pchampions_:
            self.set_purple_champion(pchampions_)

    def set_blue_champion(self, champions):
        """Sets the blue champions names"""
        for champ, button in zip(champions, self.ui.blue_buttons):
            button.setText(re.sub(r'(.*\n).*(\n.*)', r'\1' + champ + r'\2',
                           button.text()))

    def set_purple_champion(self, champions):
        """Sets the purple champions names"""
        for champ, button in zip(champions, self.ui.purple_buttons):
            button.setText(re.sub(r'(.*\n).*(\n.*)', r'\1' + champ + r'\2',
                                  button.text()))

    def set_blue_team(self, lineup):
        """Sets the blue team players"""
        for player, button in zip(lineup, self.ui.blue_buttons):
            button.setText(re.sub(r'(.*\n.*\n).*', r'\1' + player,
                                  button.text()))

    def set_purple_team(self, lineup):
        """Sets the purple team players"""
        for player, button in zip(lineup, self.ui.purple_buttons):
            button.setText(re.sub(r'(.*\n.*\n).*', r'\1' + player,
                                  button.text()))

    def uncheck_players(self):
        """Unchecks all players button"""
        for b_ in self.ui.blue_buttons + self.ui.purple_buttons:
            b_.setChecked(False)

