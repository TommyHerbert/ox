from knowledge.didnt_understand import DidntUnderstand


class NaiveConversationStrategy:
    def __init__(self):
        pass

    @staticmethod
    def construct_move(context, source_path):
        if not context:
            return NaiveConversationStrategy._didnt_understand()
        '''
        TODO: maybe now that expectations are stored separately,
        this can be simpler
        '''
        for i in range(len(context['expectations'])):
            element = context['expectations'][i]
            if element.is_expectation():
                del context['expectations'][i]
                return element.content
        return NaiveConversationStrategy._didnt_understand()

    @staticmethod
    def construct_move(context, source_path): # TODO: Need a parameter to hold the longer-term knowledge base
        if not context:
            return NaiveConversationStrategy._didnt_understand()
        if len(context['expectations']) > 0:
            content = context['expectations'][0].content
            del context['expectations'][0]
            return content
        if len(context['propositions']) > 0:
            pass # TODO: how is it stored and how is it needed?
            # TODO: compare the proposition's content to the knowledge base in the context
            # TODO: if it's there, select AlreadyKnow
            # TODO: if not, learn the relation and select ThanksForTellingMe
        return NaiveConversationStrategy._didnt_understand()

    @staticmethod
    def _didnt_understand():
        return DidntUnderstand().get_logical_form()

