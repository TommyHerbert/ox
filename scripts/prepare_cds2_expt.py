from knowledge.knowledge_base import KnowledgeBase
from knowledge.concept import Thing
from knowledge.song import Song
from utils.knowledge import create_unique_package
from os.path import join

TOP_LEVEL = '/home/oxadmin/ox'



def closer_init(closer_self):
    Thing.__init__(closer_self)
    closer_self.lexical_form = 'Closer'


knowledge_base = KnowledgeBase()
Closer = type('Closer', (Thing,), dict(__init__=closer_init))
closer = Closer()
knowledge_base.add_thing(closer)
song = Song()
knowledge_base.categories.append(song)
knowledge_base.add_relation('is_a', (closer, song))
new_knowledge = 'new_knowledge'
unique_id = create_unique_package(join(TOP_LEVEL, new_knowledge))
target_package = join(new_knowledge, unique_id)
knowledge_base.write_package(TOP_LEVEL, 'knowledge', target_package)

