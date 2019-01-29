import logging
from os import path, makedirs, listdir, remove
from importlib import import_module
from utils.knowledge import create_empty_package
from shutil import rmtree

LOG_PATH = '/home/oxadmin/ox/logs'
MERGED_PATH = '/home/oxadmin/ox/merged_knowledge'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)
logging.basicConfig(level=logging.INFO, filename=LOG_PATH + '/cds2.log')
logging.info('started cds2')


def build_knowledge_base(location):
    prefix = location + '.'
    knowledge_base = import_module(prefix + 'knowledge_base').KnowledgeBase()
    populator_module = import_module(prefix + 'knowledge_base_populator')
    populator_module.KnowledgeBasePopulator.populate(knowledge_base)
    return knowledge_base


# build old knowledge base
current_version = build_knowledge_base('knowledge')

# build the new knowledge bases and merge them into the old one
new_packages = [x for x in listdir('new_knowledge') if x != '__init__.py']
for package_name in new_packages:
    location = 'new_knowledge.' + package_name
    current_version = current_version.merge(build_knowledge_base(location))

# create merged_knowledge package if necessary
create_empty_package(MERGED_PATH)

# write the merged knowledge base to a temporary location
current_version.write_package('knowledge', 'merged_knowledge')

# clear out the new_knowledge package
for package in new_packages:
    rmtree(path.join('new_knowledge', package))

# write the new knowledge base to its final resting place
current_version.write_package('merged_knowledge', 'knowledge')

# clear out the merged_knowledge package
for name in [x for x in listdir('merged_knowledge') if x != '__init__.py']:
    if path.isdir(name):
        rmtree(name)
    else:
        remove(name)

logging.info('completed cds2')

