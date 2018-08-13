from utils.case import headline_to_snake
from os.path import join
from os import makedirs
from pathlib import Path


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
        with open(populator_path, 'w') as populator_file:
            for concept in self.categories + self.things:
                populator_file.write(concept.get_import_statement(path) + '\n')
                # TODO: extract package path creation from
                # get_import_statement
            # TODO


    def matches(self, knowledge_base):
        pass # TODO

