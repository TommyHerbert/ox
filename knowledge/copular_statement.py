from knowledge.concept import Thing
from knowledge.statement import Statement
import re
from functools import partial
from knowledge.logical_tree import LogicalTreeBranch, LogicalTreeLeaf
from utils.case import phrase_to_headline


class CopularStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def get_statement_logic(self, input_string, knowledge_base, reader):
        arguments = self.get_arguments(input_string)
        if not arguments:
            return None
        instance_name_leaf = LogicalTreeLeaf(arguments[0])
        category_leaf = reader.parse(arguments[1], knowledge_base)
        if not category_leaf:
            return None
        copular = partial(self.add_belief, knowledge_base)
        return LogicalTreeBranch(copular, [instance_name_leaf, category_leaf])

    @staticmethod
    def get_arguments(input_string):
        match = re.match("(.+) is a (.+)\.", input_string)
        return [match.group(1), match.group(2)] if match else None

    def add_belief(self, knowledge_base, instance_name, category):
        thing = self.make_thing(instance_name)
        knowledge_base.add_thing(thing)
        knowledge_base.add_relation('is_a', [thing, category])

    @staticmethod
    def make_thing(instance_name):
        class_name = phrase_to_headline(instance_name)
        new_thing_type = type(class_name, (Thing,), dict())
        thing = new_thing_type()
        thing.lexical_form = instance_name
        return thing

