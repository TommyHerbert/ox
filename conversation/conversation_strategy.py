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
    def _didnt_understand():
        return DidntUnderstand().get_logical_form()

