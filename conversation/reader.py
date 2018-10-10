'''
TODO: may be able to remove the class and have top-level functions
instead of methods
'''
class Reader:
    def read_last_move(self, conversation):
        logical_form = self.parse(conversation.utterances[-1].text,
                                  conversation.context['knowledge_base'])
        if not logical_form:
            return
        element_type = logical_form.element_type()
        conversation.context[element_type].append(logical_form)

    def parse(self, utterance, knowledge_base):
        for category in knowledge_base.categories:
            logical_form = category.get_logical_form(utterance,
                                                     knowledge_base,
                                                     self)
            if logical_form:
                return logical_form
        return None

