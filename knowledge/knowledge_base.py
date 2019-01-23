from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path
from utils.paths import to_package_path
from utils.lists import sorted_copy, merge_lists
from distutils.dir_util import copy_tree
from knowledge.relation import get_relation_import_statement, Relation

populator_template = '''{imports}


class KnowledgeBasePopulator:
    def populate(knowledge_base):
        {instantiation}
        
        {populate_categories}

        {populate_things}

        {populate_relations}

'''


class KnowledgeBase:
    def __init__(self):
        self.categories = []
        self.things = []
        self.relations = []

    def is_empty(self):
        return self.categories + self.things + self.relations == []
    
    def export_populator(self, path):
        populator_path = join(path, 'knowledge_base_populator.py')
        separator = '\n' + 8 * ' '
        imports = self.get_imports(path)
        concepts = self.categories + self.things
        instantiation = self.get_instantiation_statements(concepts, separator)
        populate_categories = \
            self.get_population_statements(self.categories, separator)
        populate_things = \
            self.get_population_statements(self.things, separator)
        populate_relations = self.get_addition_logic(self.relations, separator)
        populator_source = populator_template.format(**vars())
        with open(populator_path, 'w') as populator_file:
            populator_file.write(populator_source)
        for concept in concepts:
            concept.overwrite_copy(path)

    def get_imports(self, path):
        concepts = self.categories + self.things
        imports = [c.get_import_statement(path) for c in concepts]
        imports.append(get_relation_import_statement(path))
        return '\n'.join(imports)

    def get_instantiation_statements(self, concepts, separator):
        statements = [c.get_instantiation_statement() for c in concepts]
        return separator.join(statements)

    def get_population_statements(self, concepts, separator):
        return separator.join([c.get_population_statement() for c in concepts])

    def get_addition_logic(self, relations, separator):
        return separator.join([r.get_addition_statement() for r in relations])

    def matches(self, other):
        return sorted_copy(self.categories) == sorted_copy(other.categories) \
           and sorted_copy(self.things) == sorted_copy(other.things) \
           and sorted_copy(self.relations) == sorted_copy(other.relations)

    def copy(self):
        new_knowledge_base = KnowledgeBase()
        new_knowledge_base.things = list(self.things)
        new_knowledge_base.categories = list(self.categories)
        new_knowledge_base.relations = list(self.relations)
        return new_knowledge_base

    def add_thing(self, thing):
        if thing not in self.things:
            self.things.append(thing)

    def add_relation(self, name, arguments):
        self.relations.append(Relation(name, arguments))

    def merge(self, other):
        merged = KnowledgeBase()
        # TODO: Would be nicer to store these lists as sets?
        merged.categories = merge_lists(self.categories, other.categories)
        merged.things = merge_lists(self.things, other.things)
        merged.relations = merge_lists(self.relations, other.relations)
        return merged

    def write_package(self, path):
        # TODO: maybe the source path should be parametrised too
        # the app knows about it somewhere (LearningStrategy?)
        # and CDS could know about it and pass it in too
        copy_tree('knowledge', path)
        for concept in self.things + self.categories:
            concept.overwrite_copy(path)
        self.export_populator(path)
