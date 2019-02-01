from knowledge.concept import Category
from conversation.context import Proposition


class Statement(Category):
    def __init__(self):
        Category.__init__(self)

    def get_logical_form(self, input_string, knowledge_base, reader):
        if None in [input_string, knowledge_base, reader]:
            return None
        statement_logic = \
            self.get_statement_logic(input_string, knowledge_base, reader)
        return Proposition(statement_logic) if statement_logic else None

    def get_statement_logic(self, input_string, knowledge_base, reader):
        return None

    def overwrite_copy(self, source_directory, relative_path):
        pass # don't generate this concept from the default template

