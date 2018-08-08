import unittest
from app import create_app, db
from app.models import Speaker, Conversation, Utterance
from config import Config
from knowledge.song import Song


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestSelfWriting(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.ox = Speaker(email='project.ox.mail@gmail.com')
        self.test_user = Speaker(email='test@users.com')
        for s in [self.ox, self.test_user]:
            db.session.add(s)
        db.session.commit()

        self.conversation = Conversation.create()
        for s in [self.ox, self.test_user]:
            self.conversation.speakers.append(s)
        db.session.add(self.conversation)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_import_statement(self):
        expected = 'from knowledge.song import Song'
        self.assertEqual(expected, Song().get_import_statement())

