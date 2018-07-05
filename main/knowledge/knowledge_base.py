from main.utils.case import headline_to_snake
from main.knowledge.favourite_question import FavouriteQuestion
from main.knowledge.relation import Relation
from main.knowledge.song import Song
from main.knowledge.someone_like_you import SomeoneLikeYou
from main.knowledge.hello import Hello
from main.knowledge.singer import Singer
from main.knowledge.adele import Adele
from main.knowledge.compound_noun import CompoundNoun


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

        self.categories.append(FavouriteQuestion())
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

    def write(self):
        imports = ['from main.utils.case import headline_to_snake']
        for category in self.categories:
            class_name = category.__class__.__name__
            module_name = headline_to_snake(class_name)
            imports.append('from {} import {}'.format(module_name, class_name))
            # TODO
        # TODO
