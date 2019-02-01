from knowledge.concept import Category
from conversation.context import Expectation


class Question(Category):
    def __init__(self):
        Category.__init__(self)

    def get_logical_form(self,
                         input_string=None,
                         knowledge_base=None,
                         reader=None):
        if None in [input_string, knowledge_base, reader]:
            return None
        question_logic = \
            self.get_question_logic(input_string, knowledge_base, reader)
        return Expectation(question_logic) if question_logic else None

    def get_question_logic(self, input_string, knowledge_base, reader):
        return None

    def overwrite_copy(self, source_directory, relative_path):
        pass # don't generate this concept from the default template

