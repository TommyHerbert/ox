from unittest import TestCase
from main.ox import Ox
from main.conversation.conversation import Conversation


class TestOx(TestCase):
    def test_song(self):
        conversation = Conversation()
        conversation.moves.append("What's your favourite song?")
        Ox().tell(conversation)
        self.assertEqual('Hello', conversation.moves[-1])

    def test_adele_song(self):
        conversation = Conversation()
        conversation.moves.append("What's your favourite Adele song?")
        Ox().tell(conversation)
        self.assertEqual('Hello', conversation.moves[-1])

    def test_dont_understand(self):
        conversation = Conversation()
        conversation.moves.append('Hello Ox.')
        Ox().tell(conversation)
        self.assertEqual("Sorry, I didn't understand that.", conversation.moves[-1])

    def test_favourite_foo(self):
        conversation = Conversation()
        conversation.moves.append("What's your favourite foo?")
        Ox().tell(conversation)
        self.assertEqual("Sorry, I didn't understand that.", conversation.moves[-1])

    def test_favourite_foo_song(self):
        conversation = Conversation()
        conversation.moves.append("What's your favourite foo song?")
        Ox().tell(conversation)
        self.assertEqual("Sorry, I didn't understand that.", conversation.moves[-1])

    def test_favourite_adele_foo(self):
        conversation = Conversation()
        conversation.moves.append("What's your favourite Adele foo?")
        Ox().tell(conversation)
        self.assertEqual("Sorry, I didn't understand that.", conversation.moves[-1])

    def test_hello(self):
        conversation = Conversation()
        conversation.moves.append('Hello')
        Ox().tell(conversation)
        self.assertEqual("Sorry, I didn't understand that.", conversation.moves[-1])
