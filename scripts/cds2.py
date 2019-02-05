import logging
from os import path, makedirs, listdir, remove
from importlib import import_module
from utils.knowledge import create_empty_package
from shutil import rmtree

KNOWLEDGE_NAME = 'knowledge'
NEW_KNOWLEDGE_NAME = 'new_knowledge'
MERGED_NAME = 'merged_knowledge'

TOP_LEVEL = '/home/oxadmin/ox'
LOG_DIRECTORY = path.join(TOP_LEVEL, 'logs')
LOG_FILE = path.join(TOP_LEVEL, 'logs', 'cds2.log')
KNOWLEDGE_PATH = path.join(TOP_LEVEL, KNOWLEDGE_NAME)
NEW_KNOWLEDGE_PATH = path.join(TOP_LEVEL, NEW_KNOWLEDGE_NAME)
MERGED_PATH = path.join(TOP_LEVEL, MERGED_NAME)


def build_package_path(head, tail):
    return '.'.join((head, tail))


def clear_package(dir_path):
    for name in [x for x in listdir(dir_path) if x != '__init__.py']:
        file_path = path.join(dir_path, name)
        if path.isdir(file_path):
            rmtree(file_path)
        else:
            remove(file_path)


def build_knowledge_base(location):
    base_module_path = build_package_path(location, 'knowledge_base')
    knowledge_base = import_module(base_module_path).KnowledgeBase()
    populator_module_path = \
        build_package_path(location, 'knowledge_base_populator')
    populator_module = import_module(populator_module_path)
    populator_module.KnowledgeBasePopulator.populate(knowledge_base)
    return knowledge_base


# configure log
if not path.exists(LOG_DIRECTORY):
    makedirs(LOG_DIRECTORY)
logging.basicConfig(level=logging.INFO, filename=LOG_FILE)

# report that the script has started
logging.info('started cds2')

# build old knowledge base
current_version = build_knowledge_base(KNOWLEDGE_NAME)

# build the new knowledge bases and merge them into the old one
non_packages = ['__init__.py', '__pycache__']
contents = listdir(NEW_KNOWLEDGE_PATH)
for package_name in [x for x in contents if x not in non_packages]:
    location = build_package_path(NEW_KNOWLEDGE_NAME, package_name)
    current_version = current_version.merge(build_knowledge_base(location))

# create merged_knowledge package if necessary
create_empty_package(MERGED_PATH)

# write the merged knowledge base to a temporary location
current_version.write_package(TOP_LEVEL, KNOWLEDGE_NAME, MERGED_NAME)

# clear out the new_knowledge package
clear_package(NEW_KNOWLEDGE_PATH)

# write the new knowledge base to its final resting place
current_version.write_package(TOP_LEVEL, MERGED_NAME, KNOWLEDGE_NAME)

# clear out the merged_knowledge package
clear_package(MERGED_PATH)

# report that the script is finished
logging.info('completed cds2')

