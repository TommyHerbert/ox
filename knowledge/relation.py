from os.path import normpath, sep
from utils.paths import to_package_path


class Relation:
    def __init__(self, relation_type, arguments):
        self.relation_type = relation_type
        self.arguments = arguments

    def __lt__(self, other):
        if self.relation_type < other.relation_type:
            return True
        if other.relation_type < self.relation_type:
            return False
        self_args_length = len(self.arguments)
        other_args_length = len(other.arguments)
        if self_args_length < other_args_length:
            return True
        if other_args_length < self_args_length:
            return False
        for i in range(self_args_length):
            if self.arguments[i] < other.arguments[i]:
                return True
            if other.arguments[i] < self.arguments[i]:
                return False
        return False

    def __eq__(self, other):
        self_args_length = len(self.arguments)
        if self.relation_type == other.relation_type and \
           self_args_length == len(other.arguments):
            for i in range (self_args_length):
                if self.arguments[i] != other.arguments[i]:
                    return False
            return True
        return False


def has_lexical_form(relation, lexical_form):
    for argument in relation.arguments:
        try:
            if argument.get_lexical_form() == lexical_form:
                return True
        except AttributeError:
            return False
    return False


def get_relation_import_statement(path=''):
    template = 'from {}knowledge.relation import Relation'
    return template.format(to_package_path(path, final_dot=True))

