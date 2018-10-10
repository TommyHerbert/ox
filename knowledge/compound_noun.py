from functools import partial
from knowledge.logical_tree import LogicalTreeBranch
from knowledge.relation import has_lexical_form
from knowledge.concept import Category


class CompoundNoun(Category):
    def __init__(self):
        pass

    def get_logical_form(self, input_string, knowledge_base, reader):
        words = input_string.split()
        if len(words) != 2:
            return None
        category = reader.parse(words[1], knowledge_base)
        if not category:
            return None
        find_referents = partial(self.find_referents, words[0], knowledge_base)
        return LogicalTreeBranch(find_referents, [category])

    def find_referents(self, qualifier_string, knowledge_base, category):
        def instance(r):
            return r.relation_type == 'is_a' and r.arguments[1] == category
        relations = knowledge_base.relations
        instances = [r.arguments[0] for r in relations if instance(r)]
        related = lambda i: self.is_related(i, qualifier_string, relations)
        return [i for i in instances if related(i)]

    def overwrite_copy(self, path):
        pass # don't generate this concept from the default template

    @staticmethod
    def is_related(obj, lexical_form, relations):
        def relevant(r):
            return obj in r.arguments and has_lexical_form(r, lexical_form)
        return len([r for r in relations if relevant(r)]) > 0

