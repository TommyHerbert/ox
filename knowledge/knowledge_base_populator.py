from knowledge.singer import Singer
from knowledge.song import Song
from knowledge.compound_noun import CompoundNoun
from knowledge.favourite_question import FavouriteQuestion
from knowledge.myself import Myself
from knowledge.adele import Adele
from knowledge.hello import Hello
from knowledge.someone_like_you import SomeoneLikeYou
from knowledge.relation import Relation

class KnowledgeBasePopulator:
    def populate(knowledge_base):
        # instantiate categories
        singer = Singer()
        song = Song()
        compound_noun = CompoundNoun()
        favourite_question = FavouriteQuestion()

        # instantiate things
        myself = Myself()
        adele = Adele()
        hello = Hello()
        someone_like_you = SomeoneLikeYou()

        # populate categories
        knowledge_base.categories.append(singer)
        knowledge_base.categories.append(song)
        knowledge_base.categories.append(compound_noun)
        knowledge_base.categories.append(favourite_question)

        # populate things
        knowledge_base.things.append(myself)
        knowledge_base.things.append(adele)
        knowledge_base.things.append(hello)
        knowledge_base.things.append(someone_like_you)

        # populate relations
        def add_relation(name, args):
            knowledge_base.relations.append(Relation(name, args))
        add_relation('is_a', (adele, singer))
        add_relation('is_a', (hello, song))
        add_relation('is_a', (someone_like_you, song))
        add_relation('sang', (adele, hello))
        add_relation('sang', (adele, someone_like_you))
        add_relation('likes', (myself, hello, 1000))
        add_relation('likes', (myself, someone_like_you, 900))

