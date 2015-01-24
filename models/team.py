import json
import codecs
import string


class Team():
    """Defines a team

    Team has a name, tag and are composed by 5 players. The tag property is used
    as unique identifier of team for save export/import purposes"""

    def __init__(self):
        self.name = ''
        self.tag = ''
        self.top = ''
        self.jungle = ''
        self.mid = ''
        self.adc = ''
        self.support = ''

    def load_json(self):
        """Loads a team from a JSON file store in `./teams/` directory. The file
        should be named `tag.json`"""
        file_obj = codecs.open(u"./teams/" + self.tag + ".json", "r", "utf-8")
        data = json.load(file_obj)

        attr = ['name', 'tag', 'top', 'mid', 'jungle', 'adc', 'support']

        for a_ in attr:
            setattr(self, a_, data[a_])

    def save_json(self):
        """Saves a team as a `tag.json` JSON file in the `./teams/` directory"""
        with codecs.open(u"./teams/" + self.tag + ".json", "w", "utf-8") as f:
            json.dump(self, f, cls=TeamEncoder)

    def populate(self, name, tag, top, jungle, mid, adc, support):
        """Populates a team with properties

        :param name: the team's name
        :type name: string
        :param tag: the team's tag (conventionally 3 letters)
        :type tag: string
        :param top: top player's name
        :type top: string
        :param jungle: jungle player's name
        :type jungle: string
        :param mid: mid player's name
        :type mid: string
        :param adc: adc player's name
        :type adc: string
        :param support: support player's name
        :type support: string
        """
        self.name = name
        self.tag = tag
        self.top = top
        self.mid = mid
        self.jungle = jungle
        self.adc = adc
        self.support = support

    def __str__(self):
        """Returns a string description of the team for console display
        :returns: '/' separated string
        :rtype: string"""
        return '/'.join([self.name, self.tag, self.top, self.jungle, self.mid,
                         self.adc, self.support])


class TeamEncoder(json.JSONEncoder):
    """Defines a JSON team encoder for export purposes
    
    Typical use: 

    .. code-block:: python

       json.dump(self, f, cls=TeamEncoder)
    """
    def default(self, o):
        return o.__dict__
