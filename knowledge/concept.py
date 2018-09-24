from utils.case import headline_to_snake
from utils.paths import to_package_path
from knowledge.logical_tree import LogicalTreeLeaf
from os.path import normpath, sep, join


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

    def __eq__(self, other):
        return self.get_class_name() == other.get_class_name()

    def __lt__(self, other):
        return self.get_class_name() < other.get_class_name()

    def get_module_name(self):
        return headline_to_snake(self.get_class_name())
    
    def get_import_statement(self, path=''):
        package_path = to_package_path(path, final_dot=True)
        return 'from {}knowledge.{} import {}'.format(package_path,
                                                      self.get_module_name(),
                                                      self.get_class_name())

    def get_instantiation_statement(self):
        return '{} = {}()'.format(self.get_module_name(),
                                  self.get_class_name())

    def get_concept_type(self):
        return 'UndefinedConceptType'

    def write(self, path):
        # TODO: this bit is shared with KnowledgeBase.export_populator
        knowledge_path = join(path, 'knowledge')
        makedirs(knowledge_path)
        Path(join(knowledge_path, '__init__.py')).touch()

        module_path = join(knowledge_path, self.get_module_name()) + '.py'
        concept_type = self.get_concept_type()
        with open(module_path, 'w') as module_file:
            pass # TODO


class Category(Concept):
    def __init__(self):
        Concept.__init__(self)

    def get_concept_type(self):
        return 'Category'


class Thing(Concept):
    def __init__(self):
        Concept.__init__(self)

    def get_concept_type(self):
        return 'Thing'

