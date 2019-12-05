# Implement a class to hold room information. This should have name and description attributes.


class Room:

    def __init__(self, name, description, bounty=[]):
        self.name = name
        self.description = description
        self.bounty = bounty
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'{self.description}'

    def collect(self, item):
        self.bounty.append(item)

    def taken(self, item):
        self.bounty.remove(item)

