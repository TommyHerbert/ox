from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path
from utils.paths import to_package_path


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
        populator_template = '''{}

class KnowledgeBasePopulator:
    def populate(knowledge_base):
        {}
        
        {}
'''
        with open(populator_path, 'w') as populator_file:
            for concept in self.categories + self.things:
                populator_file.write(concept.get_import_statement(path) + '\n')
            knowledge_package_path = to_package_path(knowledge_path)
            relation_import_template = 'from {}.relation import Relation\n'
            relation_import = \
                relation_import_template.format(knowledge_package_path)
            # TODO


    def matches(self, knowledge_base):
        pass # TODO

