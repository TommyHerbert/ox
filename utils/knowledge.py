from os import makedirs
from os.path import join
from pathlib import Path


def create_knowledge_package(path):
    knowledge_path = join(path, 'knowledge')
    makedirs(knowledge_path)
    Path(join(path, '__init__.py')).touch()
    Path(join(knowledge_path, '__init__.py')).touch()

