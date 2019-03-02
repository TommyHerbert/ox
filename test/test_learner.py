from unittest import TestCase
from utils.knowledge import create_empty_package
from knowledge.knowledge_base import KnowledgeBase
from knowledge.adele import Adele
from knowledge.singer import Singer
from learner import update
from shutil import rmtree
from os.path import join

OUTPUT_PATH = 'learner_test_output'


class TestLearner(TestCase):
    def setUp(self):
        create_empty_package(join(OUTPUT_PATH, 'new_knowledge'))

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
        '''
        TODO:
        confirm bases now match
        create and populate knowledge base from new knowledge package
        confirm that one matches the other two as well
        '''

