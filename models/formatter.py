from data import formats
import random


class Formatter():
    """Engine to format strings according to the available formats in
    data.formats"""

    def __init__(self):
        pass

    def format_player(name_, team_, position_, champion_):
        return formats.player.format(name=name_,
                                     team=Formatter.format_team(team_),
                                     position=position_, champion=champion_)

    def format_team(tag_):
        return formats.team.format(team=tag_)

    def format_kill(namea_, teama_, positiona_, championa_, 
                   nameb_, teamb_, positionb_, championb_):
        return Formatter.randlist(formats.kill).format(
            Formatter.format_player(namea_, teama_, positiona_, championa_),
            Formatter.format_player(nameb_, teamb_, positionb_, championb_))

    def format_dragon(team_, stack_):
        return Formatter.randlist(formats.dragon).format(
            team=Formatter.format_team(team_), stack=stack_)

    def format_baron(team_, stack_):
        return Formatter.randlist(formats.baron).format(
            Formatter.format_team(team=team_), stack=stack_)

    def randlist(list_):
        return list_[random.randrange(len(list_))]


