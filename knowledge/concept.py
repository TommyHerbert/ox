from utils.case import headline_to_snake
from knowledge.logical_tree import LogicalTreeLeaf


class Concept:
    def __init__(self):
        self.lexical_form = None

    def get_lexical_form(self):
        return self.lexical_form

    def get_logical_form(self, input_string=None, reader=None):
        if input_string in [None, self.lexical_form]:
            return LogicalTreeLeaf(self)
        else:
            return None

    def get_class_name(self):
        return self.__class__.__name__

    def get_module_name(self):
        return headline_to_snake(self.get_class_name())
    
    def get_import_statement(self):
        template = 'from knowledge.{} import {}'
        return template.format(self.get_module_name(), self.get_class_name())

    def get_instantiation_statement(self):
        return '{} = {}()'.format(self.get_module_name(),
                                  self.get_class_name())


class Category(Concept):
    def __init__(self):
        Concept.__init__(self)


class Thing(Concept):
    def __init__(self):
        Concept.__init__(self)

