from main.knowledge.concept import Thing
from main.knowledge.knowledge_base import KnowledgeBase
from main.conversation.conversation import NaiveConversationStrategy
from main.conversation.reader import Reader
from main.conversation.reasoner import Reasoner
from main.conversation.speaker import Speaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.PickleType())
    #context = db.Column(db.PickledType())


class Ox(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Ox'

        # Nothing is using this yet, and anyway Ox can't yet understand
        # it. But it seems like a way to set out our stall.
        self.goal = 'do good by teaching'

        self.knowledge_base = KnowledgeBase(self)
        self.strategy = NaiveConversationStrategy()
        self.reader = Reader(self.knowledge_base)
        self.reasoner = Reasoner()
        self.speaker = Speaker()

    # Say something to Ox. Ox will update its model of the conversation
    # and then say something back.
    def tell(self, conversation):
        self.reader.read_last_move(conversation)
        conversation_to_persist = Conversation(context=conversation.context)
        db.session.add(conversation_to_persist)
        db.session.commit()
        fetched_conversation = \
            Conversation.query.get(conversation_to_persist.id)
        next_move = self.strategy.pop_move(fetched_conversation.context)
        answer_concept = self.reasoner.take_move(next_move)
        conversation.moves.append(self.speaker.utter(answer_concept))

