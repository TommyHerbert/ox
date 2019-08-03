from knowledge.didnt_understand import DidntUnderstand


class NaiveConversationStrategy:
    def __init__(self, knowledge_base, reasoner):
        self.knowledge_base = knowledge_base
        self.reasoner = reasoner

    def construct_move(context, source_path):
        if not context:
            return NaiveConversationStrategy._didnt_understand()
        if len(context['expectations']) > 0:
            content = context['expectations'][0].content
            del context['expectations'][0]
            return content
        if len(context['propositions']) > 0:
            content = context['propositions'][0].content
            del context['propositions'][0]
            # TODO: I need a stack class so the calling code doesn't
            #       mess about with duplicated popping logic

            # So now I have a logical tree which should be resolved
            # in the same way that the reasoner resolves expectation
            # trees. Maybe I should ask the reasoner to do so? But
            # first I should take a copy of the knowledge base in
            # the context so I can see if the resolution made a
            # difference.
            temporary_base = context['knowledge_base'].copy()

            # TODO: if the knowledge base changes, select ThanksForTellingMe and notify the Learner
            # TODO: if not, select AlreadyKnow
        return NaiveConversationStrategy._didnt_understand()

    @staticmethod
    def _didnt_understand():
        return DidntUnderstand().get_logical_form()

