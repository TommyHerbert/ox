from question import FavouriteQuestion
from relation import Relation
from song import Song, Hello, SomeoneLikeYou
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
        someone_like_you = SomeoneLikeYou()
        compound_noun = CompoundNoun()

        self.categories.append(FavouriteQuestion(self.ox))
        self.categories.append(singer)
        self.categories.append(song)
        self.categories.append(compound_noun)

        self.things.append(adele)
        self.things.append(hello)
        self.things.append(someone_like_you)

        self.relations.append(Relation('is_a', (adele, singer)))
        self.relations.append(Relation('is_a', (hello, song)))
        self.relations.append(Relation('is_a', (someone_like_you, song)))
        self.relations.append(Relation('sang', (adele, hello)))
        self.relations.append(Relation('sang', (adele, someone_like_you)))
        self.relations.append(Relation('likes', (self.ox, hello, 1000)))
        self.relations.append(Relation('likes', (self.ox, someone_like_you, 900)))
