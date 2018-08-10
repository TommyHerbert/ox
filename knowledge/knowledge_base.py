from utils.case import headline_to_snake


class KnowledgeBase:
    def __init__(self):
        self.categories = []
        self.things = []
        self.relations = []

    def is_empty(self):
        return self.categories == [] and \
               self.things == [] and \
               self.relations == []

    # TODO: maybe the Concept class should handle some of this logic
    def write(self, path):
        imports = []
        instantiations = []
        for concept in self.categories + self.things:
            import_template = 'from knowledge.{} import {}'
            class_name = category.__class__.__name__
            module_name = headline_to_snake(class_name)
            imports.append(import_template.format(module_name, class_name))
            instantiation_template = '{} = {}()'
            instantiations.append('{} = {}()'.format(module_name, class_name))
            
        imports.append('from knowledge.relation import Relation')
        imports.append('from utils.case import headline_to_snake')
        # TODO

