from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path
from utils.paths import to_package_path
from utils.lists import sorted_copy

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
        knowledge_path = join(path, 'knowledge')
        makedirs(knowledge_path)
        Path(join(knowledge_path, '__init__.py')).touch()
        populator_path = join(knowledge_path, 'knowledge_base_populator.py')
        imports = self.get_imports(path)
        concepts = self.categories + self.things
        instantiation = self.get_instantiation_statements(concepts)
        populate_categories = self.get_population_statements(self.categories)
        populate_things = self.get_population_statements(self.things)
        populate_relations = self.get_addition_logic(self.relations)
        populator_source = populator_template.format(
            imports=imports,
            instantiation=instantiation,
            populate_categories=populate_categories,
            populate_things=populate_things,
            populate_relations=populate_relations)
        with open(populator_path, 'w') as populator_file:
            populator_file.write(populator_source)

    # TODO: could probably write a test for this piece individually
    def get_imports(self, path):
        imports = ''
        for concept in self.categories + self.things:
            imports += concept.get_import_statement(path) + '\n'
        return imports[-1] # cut the trailing newline

    def get_instantiation_statements(self, concepts):
        pass # TODO

    def get_population_statements(self, concepts):
        pass # TODO

    def get_addition_logic(self, relations):
        pass # TODO

    def matches(self, other):
        return sorted_copy(self.categories) == sorted_copy(other.categories) \
           and sorted_copy(self.things) == sorted_copy(other.things) \
           and sorted_copy(self.relations) == sorted_copy(other.relations)

