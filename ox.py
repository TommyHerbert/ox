from conversation import Conversation
from reader import Reader
from knowledge_base import KnowledgeBase


class Ox:
    def __init__(self):
        self.goal = 'do good by teaching'
        self.knowledge_base = KnowledgeBase(self)
        self.conversation = Conversation()
        self.reader = Reader(self.knowledge_base)

    def tell(self, interlocutor_utterance):
        self.reader.read(interlocutor_utterance, self.conversation)
