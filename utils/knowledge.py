from os import makedirs
from os.path import join
from pathlib import Path
from uuid import uuid4
from shutil import copytree


# TODO: this one will become obsolete
def create_knowledge_package(path):
    unique_id = str(uuid4())
    knowledge_path = join(path, unique_id, 'knowledge')
    makedirs(knowledge_path)
    Path(join(path, '__init__.py')).touch()
    Path(join(path, unique_id, '__init__.py')).touch()
    Path(join(knowledge_path, '__init__.py')).touch()
    return unique_id


def create_unique_package(path):
    unique_id = str(uuid4())
    extended_path = join(path, unique_id)
    makedirs(extended_path)
    Path(join(extended_path, '__init__.py')).touch()
    return unique_id


def create_empty_knowledge_package(path):
    makedirs(join(path, 'knowledge'))
    Path(join(path, 'knowledge', '__init__.py')).touch()


def copy_knowledge_package(source, target):
    copytree(join(source, 'knowledge'), join(target, 'knowledge'))

