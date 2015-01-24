from PySide import QtCore
from .team import Team
from .lineup import Lineup


class Match(QtCore.QObject):
    """Match describes the infomation needed to process a League of Legends
    match. Typically, LoL encounters regroup two teams, each playing a
    particular champion lineup"""

    teamHasChanged = QtCore.Signal()
    lineupHasChanged = QtCore.Signal()

    def __init__(self):
        """Default initialistation of match"""
        QtCore.QObject.__init__(self)
        self._blue_team = Team()      # Team
        self._purple_team = Team()    # Team
        self._lineup = Lineup()       # Lineup

    def set_lineup(self, lineup):
        """Set the champion's lineup. Includes both blue and purple team"""
        self._lineup = lineup
        self.lineupHasChanged.emit()

    def lineup(self):
        return self._lineup

    def set_blue_team(self, team):
        """Sets the blue team

        :param team: The team to be set as blue
        :type team: Team object"""
        self._blue_team = team
        self.teamHasChanged.emit()

    def set_purple_team(self, team):
        """Sets the purple team

        :param team: The team to be set as purple
        :type team: Team"""
        self._purple_team = team
        self.teamHasChanged.emit()

    def blue_team(self):
        """Returns the blue team

        :returns: the blue team object
        :rtype: Team"""
        return self._blue_team

    def purple_team(self):
        """Returns the purple team

        :returns: the purple team object
        :rtype: Team"""
        return self._purple_team

    def list_blue_players(self):
        """Returns a list of blue players as string

        :returns: list of unformatted string of players
        :rtype: list"""
        return [self._blue_team.top, self._blue_team.jungle, self._blue_team.mid,
                self._blue_team.adc, self._blue_team.support]

    def list_purple_players(self):
        """Returns a list of purple players as string

        :returns: list of unformatted string of players
        :rtype: list"""
        return [self._purple_team.top, self._purple_team.jungle,
                self._purple_team.mid, self._purple_team.adc,
                self._purple_team.support]
