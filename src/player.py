# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def take(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)
