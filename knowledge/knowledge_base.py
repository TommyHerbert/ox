from utils.case import headline_to_snake


class KnowledgeBase:
    def __init__(self):
        self.categories = []
        self.things = []
        self.relations = []

    def is_empty(self):
        return self.categories + self.things + self.relations == []

