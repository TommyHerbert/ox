import logging
from os import path, makedirs, listdir
from importlib import import_module
from pathlib import Path

LOG_PATH = '/home/oxadmin/ox/logs'
MERGED_PATH = '/home/oxadmin/ox/merged_knowledge'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)
logging.basicConfig(level=logging.INFO, filename=LOG_PATH + '/cds2.log')
logging.info('started cds2')


def build_knowledge_base(location):
    prefix = location + '.'
    knowledge_base = import_module(location + 'knowledge_base').KnowledgeBase()
    populator_module = import_module(location + 'knowledge_base_populator')
    populator_module.KnowledgeBasePopulator.populate(knowledge_base)
    return knowledge_base


# build old knowledge base
current_version = build_knowledge_base('knowledge')

# build the new knowledge bases and merge them into the old one
new_packages = [x for x in listdir('new_knowledge') if x != '__init__.py']
for package_name in new_packages:
    location = 'new_knowledge.' + package_name
    current_version = current_version.merge(build_knowledge_base(location))

# TODO: create merged_knowledge package if necessary
if not path.exists(MERGED_PATH):
    makedirs(MERGED_PATH)
    Path(path.join(MERGED_PATH, '__init__.py')).touch()

current_version.write_package('knowledge', 'merged_knowledge')

# TODO: clear out the new_knowledge package

current_version.write_package('merged_knowledge', 'knowledge')

# TODO: clear out the merged_knowledge package

logging.info('completed cds2')

