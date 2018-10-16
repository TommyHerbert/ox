from knowledge.statement import Statement
import re
from functools import partial
from knowledge.logical_tree import LogicalTreeBranch


class CopularStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def get_statement_logic(self, input_string, knowledge_base, reader):
        arguments = self.get_arguments(input_string)
        if not arguments:
            return None
        instance = reader.parse(arguments[0], knowledge_base)
        category = reader.parse(arguments[1], knowledge_base)
        copular = partial(self.add_belief, knowledge_base)
        return LogicalTreeBranch(copular, arguments)

    @staticmethod
    def get_arguments(input_string):
        match = re.match("(.+) is a (.+)\.", input_string)
        return [match.group(1), match.group(2)] if match else None

    def add_belief(self, knowledge_base, instance_name, category_name):
        thing = self.make_thing(instance_name)
        category = self.make_category(category_name)
        knowledge_base.things.append(thing)
        knowledge_base.categories.append(category)
        knowledge_base.add_relation('is_a', [thing, category])

    @staticmethod
    def make_thing(instance_name):
        # TODO

    @staticmethod
    def make_category(category_name):
        # TODO

    def overwrite_copy(self, path):
        pass # don't generate this concept from the default template

