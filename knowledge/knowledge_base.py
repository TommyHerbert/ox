from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path
from utils.paths import to_package_path
from utils.lists import sorted_copy
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
        pass # TODO

    def add_relation(self, name, arguments):
        self.relations.append(Relation(name, arguments))

