class Lineup():
    """Defines a lineup of champion

    Each team has a top, jungle, mid, adc and support champion
    """
    def __init__(self):
        pass

    def blue_top(self):
        return self.blue_top

    def blue_mid(self):
        return self.blue_mid

    def blue_jungle(self):
        return self.blue_jungle

    def blue_adc(self):
        return self.blue_adc

    def blue_support(self):
        return self.blue_support

    def purple_top(self):
        return self.purple_top

    def purple_mid(self):
        return self.purple_mid

    def purple_jungle(self):
        return self.purple_jungle

    def purple_adc(self):
        return self.purple_adc

    def purple_support(self):
        return self.purple_support

    def set_blue_top(self, champion):
        self.blue_top = champion

    def set_blue_mid(self, champion):
        self.blue_mid = champion

    def set_blue_jungle(self, champion):
        self.blue_jungle = champion

    def set_blue_adc(self, champion):
        self.blue_adc = champion

    def set_blue_support(self, champion):
        self.blue_support = champion

    def set_purple_top(self, champion):
        self.purple_top = champion

    def set_purple_mid(self, champion):
        self.purple_mid = champion

    def set_purple_jungle(self, champion):
        self.purple_jungle = champion

    def set_purple_adc(self, champion):
        self.purple_adc = champion

    def set_purple_support(self, champion):
        self.purple_support = champion

    def list_blue_champions(self):
        return [self.blue_top, self.blue_jungle, self.blue_mid, self.blue_adc,
                self.blue_support]

    def list_purple_champions(self):
        return [self.purple_top, self.purple_jungle, self.purple_mid,
                self.purple_adc, self.purple_support]

    def set_list(self, list_):
        positions = ['blue_top', 'blue_jungle', 'blue_mid', 'blue_adc',
                     'blue_support', 'purple_top', 'purple_jungle',
                     'purple_mid', 'purple_adc', 'purple_support']
        for c_, p_ in zip(list_, positions):
            setattr(self, p_, c_)
