from os.path import normpath, sep
from utils.paths import to_package_path


class Relation:
    def __init__(self, relation_type, arguments):
        self.relation_type = relation_type
        self.arguments = arguments


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

