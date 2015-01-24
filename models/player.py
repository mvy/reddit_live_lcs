from data import formats


class Player():
    def __init__(self, name, position, team, champion=''):
        self.name = name
        self.position = position
        self.team = team
        self.champion = champion

    def __str__(self):
        return formats.player.format(name=self.name, position=self.position,
                                     team=self.team, champion=self.champion)
