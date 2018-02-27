from conversation import Conversation, NaiveConversationStrategy
from reader import Reader
from knowledge.knowledge_base import KnowledgeBase
from reasoner import Reasoner
from speaker import Speaker
from knowledge.concept import Thing


class Ox(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.goal = 'do good by teaching'
        self.knowledge_base = KnowledgeBase(self)
        self.conversation = Conversation()
        self.strategy = NaiveConversationStrategy
        self.reader = Reader(self.knowledge_base)
        self.reasoner = Reasoner()
        self.speaker = Speaker()
        self.lexical_form = 'Ox'

    def tell(self, interlocutor_utterance):
        self.reader.read(interlocutor_utterance, self.conversation)
        next_move = self.strategy.pop_move(self.conversation.context)
        answer_concept = self.reasoner.take_move(next_move)
        return self.speaker.utter(answer_concept)
