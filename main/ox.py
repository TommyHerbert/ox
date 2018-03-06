from knowledge.concept import Thing
from knowledge.knowledge_base import KnowledgeBase
from conversation.conversation import Conversation, NaiveConversationStrategy
from main.conversation.reader import Reader
from main.conversation.reasoner import Reasoner
from main.conversation.speaker import Speaker


class Ox(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Ox'

        # Nothing is using this yet, and anyway Ox can't yet understand
        # it. But it seems like a way to set out our stall.
        self.goal = 'do good by teaching'

        self.knowledge_base = KnowledgeBase(self)
        self.conversation = Conversation()
        self.strategy = NaiveConversationStrategy()
        self.reader = Reader(self.knowledge_base)
        self.reasoner = Reasoner()
        self.speaker = Speaker()

    # Say something to Ox. Ox will update its model of the conversation
    # and then say something back.
    def tell(self, interlocutor_utterance):
        self.reader.read(interlocutor_utterance, self.conversation)
        next_move = self.strategy.pop_move(self.conversation.context)
        answer_concept = self.reasoner.take_move(next_move)
        return self.speaker.utter(answer_concept)
