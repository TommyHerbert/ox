from unittest import TestCase
from utils.knowledge import create_empty_package
from knowledge.knowledge_base import KnowledgeBase
from knowledge.adele import Adele
from knowledge.singer import Singer
from conversation.learner import update
from shutil import rmtree
from os import listdir
from os.path import join
from importlib import import_module

OUTPUT_PATH = 'learner_test_output'
KNOWLEDGE = 'knowledge'
NEW_KNOWLEDGE = 'new_knowledge'


def find_new_package(directory):
    return [x for x in listdir(directory) if x != '__init__.py'][0]


class TestLearner(TestCase):
    def setUp(self):
        create_empty_package(OUTPUT_PATH)
        create_empty_package(join(OUTPUT_PATH, KNOWLEDGE))
        create_empty_package(join(OUTPUT_PATH, NEW_KNOWLEDGE))

    def tearDown(self):
        rmtree(OUTPUT_PATH)

    def test_update(self):
        # create two knowledge bases and update one from the other
        longer_term_base = KnowledgeBase()
        longer_term_base.write_package('', KNOWLEDGE, join(OUTPUT_PATH, KNOWLEDGE))

        temporary_base = KnowledgeBase()
        adele = Adele()
        singer = Singer()
        temporary_base.add_thing(adele)
        temporary_base.categories.append(singer)
        temporary_base.add_relation('is_a', (adele, singer))
        update(longer_term_base, temporary_base, OUTPUT_PATH)

        # check that the longer-term knowledge base has been updated
        self.assertTrue(longer_term_base.matches(temporary_base))

        new_package = find_new_package(join(OUTPUT_PATH, NEW_KNOWLEDGE))

        # check that new_package is a non-empty string
        self.assertEqual(str, type(new_package))
        self.assertTrue(len(new_package) > 0)

        # create and populate a knowledge base from the new source code
        package_tuple = (OUTPUT_PATH, NEW_KNOWLEDGE, new_package, knowledge)
        package_path = '.'.join(package_tuple)
        knowledge_base2 = import_module(package_path + '.knowledge_base')
        populator2 = import_module(package_path + '.knowledge_base_populator')
        new_base = knowledge_base2.KnowledgeBase()
        populator2.KnowledgeBasePopulator.populate(new_base)

        # check that the new knowledge base matches the longer-term one
        self.assertTrue(longer_term_base.matches(new_base))

