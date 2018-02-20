from question import FavouriteQuestion
from relation import Relation
from song import Song, Hello


class KnowledgeBase:
    def __init__(self, ox):
        self.ox = ox
        self.categories = []
        self.things = []
        self.relations = []
        self.categories.append(FavouriteQuestion(self.ox))
        song = Song()
        self.categories.append(song)
        hello = Hello()
        self.things.append(hello)
        self.relations.append(Relation('is_a', (hello, song)))
        self.relations.append(Relation('likes', (self.ox, hello, 1000)))
