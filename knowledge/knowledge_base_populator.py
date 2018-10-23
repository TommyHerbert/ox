from knowledge.singer import Singer
from knowledge.song import Song
from knowledge.compound_noun import CompoundNoun
from knowledge.favourite_question import FavouriteQuestion
from knowledge.myself import Myself
from knowledge.adele import Adele
from knowledge.hello import Hello
from knowledge.someone_like_you import SomeoneLikeYou
from knowledge.relation import Relation


# TODO: why have this class? populate should be a top-level function
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
        knowledge_base.add_thing(myself)
        knowledge_base.add_thing(adele)
        knowledge_base.add_thing(hello)
        knowledge_base.add_thing(someone_like_you)

        # populate relations
        knowledge_base.add_relation('is_a', (adele, singer))
        knowledge_base.add_relation('is_a', (hello, song))
        knowledge_base.add_relation('is_a', (someone_like_you, song))
        knowledge_base.add_relation('sang', (adele, hello))
        knowledge_base.add_relation('sang', (adele, someone_like_you))
        knowledge_base.add_relation('likes', (myself, hello, 1000))
        knowledge_base.add_relation('likes', (myself, someone_like_you, 900))

