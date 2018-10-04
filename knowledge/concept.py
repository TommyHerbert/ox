from utils.case import headline_to_snake
from utils.paths import to_package_path
from knowledge.logical_tree import LogicalTreeLeaf
from os.path import normpath, sep, join

template = """from {package_path}.concept import {concept_type}


class {class_name}({concept_type}):
    def __init__(self):
        {concept_type}.__init__(self)
        self.lexical_form = '{lexical_form}'

"""


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
        if not isinstance(other, Concept):
            return False
        return self.get_class_name() == other.get_class_name()

    def __lt__(self, other):
        return self.get_class_name() < other.get_class_name()

    def get_module_name(self):
        return headline_to_snake(self.get_class_name())
    
    def get_import_statement(self, path=''):
        package = to_package_path(path, final_dot=True)
        module = self.get_module_name()
        class_name = self.get_class_name()
        return 'from {}{} import {}'.format(package, module, class_name)

    def get_instantiation_statement(self):
        return '{} = {}()'.format(self.get_module_name(),
                                  self.get_class_name())

    def get_concept_type(self):
        return 'UndefinedConceptType'

    def overwrite_copy(self, path):
        file_path = join(path, self.get_module_name()) + '.py'
        package_path = to_package_path(path)
        concept_type = self.get_concept_type()
        class_name = self.get_class_name()
        lexical_form = self.get_lexical_form()
        with open(file_path, 'w') as f:
            f.write(template.format(**vars()))


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

