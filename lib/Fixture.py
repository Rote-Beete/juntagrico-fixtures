from dataclasses import dataclass
from json import dumps


@dataclass
class Factory():

    def __init__(self, model, offset=0):
        self.list = []
        self.model = model
        self.offset = offset

    @dataclass
    class FixtureEntry():

        def __init__(self, parent, child):
            self.model = "juntagrico.member"
            self.pk = len(parent.list) + parent.offset
            self.fields = child

        def encode(self):
            return self.__dict__

    def add(self, child):
        self.list.append(
            self.FixtureEntry(self, child))

    def encode(self):
        return self.__dict__

    def len(self):
        return len(self.list) + self.offset

    def get_json(self):
        return dumps(self.list, default=lambda o: o.encode(), indent=4, sort_keys=True)
