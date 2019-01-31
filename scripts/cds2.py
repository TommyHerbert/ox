import logging
from os import path, makedirs, listdir, remove
from importlib import import_module
from utils.knowledge import create_empty_package
from shutil import rmtree

KNOWLEDGE_PACKAGE_NAME = 'knowledge'
NEW_KNOWLEDGE_PACKAGE_NAME = 'new_knowledge'
MERGED_PACKAGE_NAME = 'merged_knowledge'

TOP_LEVEL = '/home/oxadmin/ox'
LOG_PATH = path.join(TOP_LEVEL, 'logs', 'cds2.log')
KNOWLEDGE_PATH = path.join(TOP_LEVEL, KNOWLEDGE_PACKAGE_NAME)
NEW_KNOWLEDGE_PATH = path.join(TOP_LEVEL, NEW_KNOWLEDGE_PACKAGE_NAME)
MERGED_PATH = path.join(TOP_LEVEL, MERGED_PACKAGE_NAME)

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)
logging.basicConfig(level=logging.INFO, filename=LOG_PATH)
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
non_packages = ['__init__.py', '__pycache__']
contents = listdir(NEW_KNOWLEDGE_PATH)
new_packages = [x for x in contents if x not in non_packages]
for package_name in new_packages:
    location = 'new_knowledge.' + package_name
    current_version = current_version.merge(build_knowledge_base(location))

# create merged_knowledge package if necessary
create_empty_package(MERGED_PATH)

# write the merged knowledge base to a temporary location
current_version.write_package(KNOWLEDGE_PATH, MERGED_PATH)

# clear out the new_knowledge package
for package in new_packages:
    rmtree(path.join(NEW_KNOWLEDGE_PATH, package))

# write the new knowledge base to its final resting place
current_version.write_package(MERGED_PATH, KNOWLEDGE_PATH)

# clear out the merged_knowledge package
for name in [x for x in listdir(MERGED_PATH) if x != '__init__.py']:
    filepath = path.join(MERGED_PATH, name)
    if path.isdir(filepath):
        rmtree(filepath)
    else:
        remove(filepath)

logging.info('completed cds2')

