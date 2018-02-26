from functools import partial
from main.logical_tree import LogicalTreeBranch


class CompoundNoun:
    def __init__(self):
        pass

    def get_logical_form(self, input_string, reader):
        words = input_string.split()
        if len(words) != 2:
            return None
        category = reader.parse(words[1])
        return LogicalTreeBranch(partial(self.find_referents, words[0], reader), [category])

    def find_referents(self, qualifier_string, reader, category):
        relations = reader.get_relations()
        # this should be a utility function in relations.py
        instances = [r.arguments[0] for r in relations if r.relation_type == 'is_a' and r.arguments[1] == category]
        # might need some classes for leaves and branches in the lexical tree
        return [i for i in instances if self.is_related(i, qualifier_string, relations)]

    def is_related(self, obj, lexical_form, relations):
        # ah, so to be fair, CompoundNoun and Question ought to provide get_lexical_form
        # is there a nicer 'exists' function or something?
        relevant_relations = [r for r in relations if obj in r.arguments and self.has_lexical_form(r, lexical_form)]
        return len(relevant_relations) > 0

    # this too could be moved to relations.py
    # and again, I expect this could be more concise
    @staticmethod
    def has_lexical_form(relation, lexical_form):
        for argument in relation.arguments:
            try:
                if argument.get_lexical_form() == lexical_form:
                    return True
            except AttributeError:
                return False
        return False
