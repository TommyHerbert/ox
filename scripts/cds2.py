from os import path, makedirs

LOG_PATH = '/home/oxadmin/ox/logs'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)

import logging

logging.basicConfig(level=logging.INFO, filename=LOG_PATH + '/cds2.log')

logging.info('started cds2')

TEMP_PATH = '/tmp/ox/'

# build old knowledge base
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
old_knowledge_base = KnowledgeBase()
KnowledgeBasePopulator.populate(old_knowledge_base)

# build new knowledge base
from new_knowledge.knowledge.knowledge_base \
    import KnowledgeBase as NewKnowledgeBase
from new_knowledge.knowledge.knowledge_base_populator \
    import KnowledgeBasePopulator as NewKnowledgeBasePopulator
new_knowledge_base = NewKnowledgeBase()
NewKnowledgeBasePopulator.populate(new_knowledge_base)

# merge the two knowledge bases
merged_knowledge_base = knowledge_base.merge(new_knowledge_base)

# write the merged knowledge base to temporary location
if not path.exists(TEMP_PATH):
    makedirs(TEMP_PATH)
merged_knowledge_base.write_package(TEMP_PATH)

logging.info('completed cds2')
