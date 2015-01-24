from PySide import QtCore, QtGui
from view.ui import live_ui
from data import formats
from models import formatter

import supervisor
import re
import pyperclip

"""List of lambdas to split object_names"""

"""Split by '_'"""
split_lambda = lambda name: name.split('_')
"""Get the last element of a '_' separated words"""
position_lambda = lambda name: split_lambda(name)[-1]
"""Get the second element of a '_' separated words"""
action_lambda = lambda name: split_lambda(name)[1]
"""Get the first elelment of a '_' seprated words"""
colour_lambda = lambda name: split_lambda(name)[0]

class LiveW(QtGui.QWidget, live_ui.Ui_Form):
    """Live view form

    Displays the elements to create a game sequence and get the corresponding
    reddit-formatted string"""

    sequenceChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(LiveW, self).__init__(parent)

        # Live UI
        self.ui = live_ui.Ui_Form()
        self.ui.setupUi(self)

        # Buttons as lists
        self.ui.blue_buttons = [self.ui.blue_top, self.ui.blue_jungle,
                                self.ui.blue_mid, self.ui.blue_adc,
                                self.ui.blue_support]

        self.ui.purple_buttons = [self.ui.purple_top, self.ui.purple_jungle,
                                  self.ui.purple_mid, self.ui.purple_adc,
                                  self.ui.purple_support]

        self.ui.action_buttons = [self.ui.action_none_button,
                                  self.ui.action_kill_button]

        self.ui.objectives_buttons = [self.ui.blue_dragon,
                                      self.ui.purple_dragon, self.ui.blue_baron,
                                      self.ui.purple_baron]

        # Sequence for kill registration
        self.sequence = []
        self.clip = ''

        # Bind buttons to actions
        self.connect_actions()

        # Get the match reference
        self.match_ = supervisor.Supervisor.match()

    def uncheck_all(self):
        """Unchecks all buttons"""
        for b_ in (self.ui.blue_buttons + self.ui.purple_buttons +
                   self.ui.action_buttons):
            b_.setChecked(False)

    def uncheck_players(self):
        """Unchecks all players button"""
        for b_ in self.ui.blue_buttons + self.ui.purple_buttons:
            b_.setChecked(False)

    def connect_actions(self):
        """Connects the UI elements to the functions"""
        # Retrieving from Match
        supervisor.Supervisor.match().teamHasChanged.connect(self.update_teams)
        supervisor.Supervisor.match().lineupHasChanged.connect(
            self.update_lineup)

        # Connect blue buttons
        for b_ in self.ui.blue_buttons + self.ui.purple_buttons:
            b_.clicked.connect(self.on_player_clicked)

        # Connect action buttons
        for ab_ in self.ui.action_buttons:
            ab_.clicked.connect(self.on_action_button_clicked)

        # Connect dragon/baron buttons
        for b_ in self.ui.objectives_buttons:
            b_.clicked.connect(self.on_objective_clicked)

        # Connect sequence changed
        self.sequenceChanged.connect(self.on_sequence_changed)

        # Clear button
        self.ui.clear_button.pressed.connect(self.clear_clipboard)

    def clear_clipboard(self):
        """Uses pyperclip to clear the clipboard"""
        self.clip = ''
        pyperclip.copy(self.clip)

    def on_sequence_changed(self):
        """Manages the sequence changed even

        If the sequence is of length 3, there is a kill action to be registered
        """
        if len(self.sequence) == 3:
            # objectName : kill_action_button
            action_ = action_lambda(self.sequence[0].objectName())

            # Actor is the first registered in sequence
            actor_colour_ = colour_lambda(self.sequence[1].objectName())
            # Actee is the second registered in sequence
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

            # Treat the actions
            if action_ == "kill":
                clip_ = formatter.Formatter.format_kill(actor_, actor_team_.tag,
                                                        actor_position_,
                                                        actor_champion_, actee_,
                                                        actee_team_.tag,
                                                        actee_position_,
                                                        actee_champion_)
                if self.clip != '':
                    # Append to the clipboard : add 2 CR for reddit format
                    # FIXME: should not probably be hardcoded
                    self.clip += "\r\n\r\n"
                self.clip += clip_

                pyperclip.copy(self.clip)

                # Restart for kill action (clear the 2 buttons from list)
                self.sequence = self.sequence[:1]
                self.uncheck_players()

    def on_action_button_clicked(self):
        """Registers a new action with sequence clearing"""
        # No more checked player buttons
        self.uncheck_players()

        if self.sender().objectName() != 'action_none_button':
            self.sequence = [self.sender()]
        else:
            self.sequence = []

        # Uncheck other actions
        for b_ in [button_ for button_ in self.ui.action_buttons if button_ !=
                   self.sender()]:
            b_.setChecked(False)

    def on_objective_clicked(self):
        """Registers a new objective for a team

        Increases the counter for that team and objective"""
        colour_ = colour_lambda(self.sender().objectName())
        objective_ = position_lambda(self.sender().objectName())

        spin_ = getattr(self.ui, '_'.join([colour_, objective_, 'spin']))
        spin_.setValue(spin_.value() + 1)

        team_ = getattr(self.match_, colour_ + "_team")()
        # Clipboard copy
        clip_ = formatter.Formatter.format_dragon(team_, spin_.value())
        pyperclip.copy(clip_)

    def on_player_clicked(self):
        """When a purple button is clicked:
        - Unchecked other purple buttons when one is clicked
        - Add it to the action sequence"""
        # Extract from sender
        colour_ = colour_lambda(self.sender().objectName())
        position_ = position_lambda(self.sender().objectName())

        # Get the buttons for this colour
        buttons_ = getattr(self.ui, colour_ + "_buttons")

        # TODO: use the second list and map setChecked ?
        for b_ in [button_ for button_ in buttons_ if button_ != self.sender()]:
            b_.setChecked(False)

        # Remove any colour button from the sequence
        self.sequence = [seq_ for seq_ in self.sequence if
                         colour_lambda(seq_.objectName()) != colour_]

        # Clipboard
        self.clip_player(colour_, position_)

        # Manage sequence
        self.sequence.append(self.sender())
        self.sequenceChanged.emit()

    def clip_player(self, colour, position_):
        """Copies player information to the clipboard (uses pyperclip)"""
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
