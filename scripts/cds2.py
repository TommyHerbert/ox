from os import path, makedirs, listdir
from importlib import import_module

LOG_PATH = '/home/oxadmin/ox/logs'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)

import logging

logging.basicConfig(level=logging.INFO, filename=LOG_PATH + '/cds2.log')

logging.info('started cds2')

# build old knowledge base
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
current_version = KnowledgeBase()
KnowledgeBasePopulator.populate(current_version)

# build the new knowledge bases and merge them into the old one
new_packages = [x for x in listdir('new_knowledge') if x != '__init__.py']
for package_name in new_packages:
    package_path = 'new_knowledge.{}.'.format(package_name)
    new_knowledge_base_module = import_module(package_path + 'knowledge_base')
    new_populator_path = package_path + 'knowledge_base_populator'
    new_populator_module = import_module(new_populator_path)
    new_knowledge_base = new_knowledge_base_module.KnowledgeBase()
    new_populator_module.KnowledgeBasePopulator.populate(new_knowledge_base)
    current_version = current_version.merge(new_knowledge_base)

# TODO: create merged_knowledge package if necessary

current_version.write_package('knowledge', 'merged_knowledge')

# TODO: clear out the new_knowledge package

current_version.write_package('merged_knowledge', 'knowledge')

# TODO: clear out the merged_knowledge package

logging.info('completed cds2')

