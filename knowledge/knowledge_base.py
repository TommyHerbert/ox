from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path
from utils.paths import to_package_path

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
        populate_categories = self.get_population_statements(self.categories)
        populate_things = self.get_population_statements(self.things)
        populate_relations = self.get_addition_logic(self.relations)
        # TODO: might not need these backslashes
        populator_source = populator_template.format( \
            imports=imports, \
            populate_categories=populate_categories, \
            populate_things=populate_things, \
            populate_relations=populate_relations)
        with open(populator_path, 'w') as populator_file:
            populator_file.write(populator_source)

    # TODO: could probably write a test for this piece individually
    def get_imports(self, path):
        imports = ''
        for concept in self.categories + self.things:
            imports += concept.get_import_statement(path) + '\n'
        return imports[-1] # cut the trailing newline

    def get_population_statements(self, concepts):
        pass # TODO

#    populator_file.write(concept.get_import_statement(path) + '\n')
#knowledge_package_path = to_package_path(knowledge_path)
#relation_import_template = 'from {}.relation import Relation\n'
#relation_import = \
#    relation_import_template.format(knowledge_package_path)

    def matches(self, knowledge_base):
        pass # TODO

