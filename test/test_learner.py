from unittest import TestCase
from utils.knowledge import create_empty_package
from knowledge.knowledge_base import KnowledgeBase
from knowledge.adele import Adele
from knowledge.singer import Singer
from conversation.learner import update
from shutil import rmtree
from os.path import join
from importlib import import_module

OUTPUT_PATH = 'learner_test_output'
NEW_KNOWLEDGE = 'new_knowledge'


class TestLearner(TestCase):
    def setUp(self):
        create_empty_package(OUTPUT_PATH)
        create_empty_package(join(OUTPUT_PATH, NEW_KNOWLEDGE))

    def tearDown(self):
        rmtree(OUTPUT_PATH)

    def test_update(self):
        longer_term_base = KnowledgeBase()
        temporary_base = KnowledgeBase()
        adele = Adele()
        singer = Singer()
        temporary_base.add_thing(adele)
        temporary_base.categories.append(singer)
        temporary_base.add_relation('is_a', (adele, singer))
        update(longer_term_base, temporary_base, OUTPUT_PATH)

        self.assertTrue(longer_term_base.matches(temporary_base))

        new_package = find_new_package(join(OUTPUT_PATH, NEW_KNOWLEDGE))
        package_tuple = (OUTPUT_PATH, NEW_KNOWLEDGE, new_package, knowledge)
        package_path = '.'.join(package_tuple)
        knowledge_base2 = import_module(package_path + '.knowledge_base')
        populator2 = import_module(package_path + '.knowledge_base_populator')
        new_base = knowledge_base2.KnowledgeBase()
        populator2.KnowledgeBasePopulator.populate(new_base)
        self.assertTrue(longer_term_base.matches(new_base))

