from models import team, match


class Supervisor():
    # Single instance of match
    _match = match.Match()

    def __init__(self):
        pass

    def match():
        return Supervisor._match
