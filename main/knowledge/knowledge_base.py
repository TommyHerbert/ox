from question import FavouriteQuestion
from relation import Relation
from song import Song, Hello
from singer import Singer, Adele


class KnowledgeBase:
    def __init__(self, ox):
        self.ox = ox
        self.categories = []
        self.things = []
        self.relations = []

        singer = Singer()
        adele = Adele()
        song = Song()
        hello = Hello()

        self.categories.append(FavouriteQuestion(self.ox))
        self.categories.append(singer)
        self.categories.append(song)

        self.things.append(hello)
        self.things.append(adele)

        self.relations.append(Relation('is_a', (hello, song)))
        self.relations.append(Relation('is_a', (adele, singer)))
        self.relations.append(Relation('sang', (adele, hello)))
        self.relations.append(Relation('likes', (self.ox, hello, 1000)))
