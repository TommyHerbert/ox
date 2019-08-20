from knowledge.didnt_understand import DidntUnderstand
from knowledge.thanks_for_telling_me import ThanksForTellingMe
from knowledge.already_know import AlreadyKnow
from conversation import learner


class NaiveConversationStrategy:
    def __init__(self, knowledge_base, reasoner):
        self.knowledge_base = knowledge_base
        self.reasoner = reasoner

    def construct_move(self, context, source_path):
        if not context:
            return DidntUnderstand().get_logical_form()
        if len(context['expectations']) > 0:
            content = context['expectations'][0].content
            del context['expectations'][0]
            return content
        if len(context['propositions']) > 0:
            content = context['propositions'][0].content
            del context['propositions'][0]
            # TODO: I need a stack class so the calling code doesn't
            #       mess about with duplicated popping logic

            temporary_base = context['knowledge_base'].copy()
            self.reasoner.resolve(content)
            if temporary_base.matches(context['knowledge_base']):
                return AlreadyKnow().get_logical_form()
            else:
                learner.update(self.knowledge_base,
                               context['knowledge_base'],
                               source_path)
                return ThanksForTellingMe().get_logical_form()
        return DidntUnderstand().get_logical_form()

