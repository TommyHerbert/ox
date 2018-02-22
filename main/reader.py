class Reader:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def read(self, utterance, conversation):
        conversation.moves.append(utterance)
        conversation.context.append(self.parse(utterance))

    def parse(self, utterance):
        for category in self.knowledge_base.categories:
            logical_form = category.get_logical_form(utterance, self)
            if logical_form:
                return logical_form
        return None

    def get_relations(self):
        return self.knowledge_base.relations
