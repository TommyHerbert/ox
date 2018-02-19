from conversation import Conversation
from reader import Reader


class Ox:
    def __init__(self):
        self.goal = 'do good by teaching'
        self.conversation = Conversation()
        self.reader = Reader()

    def tell(self, interlocutor_utterance):
        self.reader.read(interlocutor_utterance, self.conversation)
