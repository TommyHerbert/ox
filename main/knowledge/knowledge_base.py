from question import FavouriteQuestion
from relation import Relation
from song import Song, Hello
from singer import Singer, Adele
from compound_noun import CompoundNoun


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
        compound_noun = CompoundNoun()

        self.categories.append(FavouriteQuestion(self.ox))
        self.categories.append(singer)
        self.categories.append(song)
        self.categories.append(compound_noun)

        self.things.append(hello)
        self.things.append(adele)

        self.relations.append(Relation('is_a', (hello, song)))
        self.relations.append(Relation('is_a', (adele, singer)))
        self.relations.append(Relation('sang', (adele, hello)))
        self.relations.append(Relation('likes', (self.ox, hello, 1000)))
