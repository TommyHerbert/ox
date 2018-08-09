import unittest
#from app import create_app, db
#from app.models import Speaker, Conversation, Utterance
#from config import Config
from knowledge.song import Song
from knowledge.adele import Adele
from knowledge.knowledge_base import KnowledgeBase


#class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestSelfWriting(unittest.TestCase):
#    def setUp(self):
#        self.app = create_app(TestConfig)
#        self.app_context = self.app.app_context()
#        self.app_context.push()
#        db.create_all()
#
#        self.ox = Speaker(email='project.ox.mail@gmail.com')
#        self.test_user = Speaker(email='test@users.com')
#        for s in [self.ox, self.test_user]:
#            db.session.add(s)
#        db.session.commit()
#
#        self.conversation = Conversation.create()
#        for s in [self.ox, self.test_user]:
#            self.conversation.speakers.append(s)
#        db.session.add(self.conversation)
#        db.session.commit()
#
#    def tearDown(self):
#        db.session.remove()
#        db.drop_all()
#        self.app_context.pop()

    def test_get_import_statement(self):
        expected = 'from knowledge.song import Song'
        self.assertEqual(expected, Song().get_import_statement())

    def test_get_instantiation_statement(self):
        expected = 'adele = Adele()'
        self.assertEqual(expected, Adele().get_instantiation_statement())

    def test_write(self):
        knowledge_base = KnowledgeBase()
        knowledge_base.write('knowledge2')
        from knowledge2 import knowledge_base.KnowledgeBase as KnowledgeBase2
        knowledge_base2 = KnowledgeBase2()
        self.assertTrue(knowledge_base.matches(knowledge_base2))
        knowledge_base2.write('test_output2')

        # TODO: check that kb3 matches kb2

        # TODO: should also check that the copies aren't borrowing
        # modules from the original

        # I guess if the test runner started by checking out the code
        # then one way to confirm would be to delete the original kb
        # from the local repo, breaking any unwanted dependencies
        

