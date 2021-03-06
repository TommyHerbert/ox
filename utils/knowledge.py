from os import makedirs
from os.path import join, isdir, exists
from pathlib import Path
from uuid import uuid4
from shutil import copytree


def create_unique_package(path):
    unique_id = 'p' + str(uuid4()).replace('-', '_')
    extended_path = join(path, unique_id)
    makedirs(extended_path)
    Path(join(extended_path, '__init__.py')).touch()
    return unique_id


def create_empty_package(path):
    if not isdir(path):
        makedirs(path)
    initialiser_path = join(path, '__init__.py')
    if not exists(initialiser_path):
        Path(initialiser_path).touch()


def create_empty_knowledge_package(path):
    makedirs(join(path, 'knowledge'))
    Path(join(path, 'knowledge', '__init__.py')).touch()


def copy_knowledge_package(source, target):
    copytree(join(source, 'knowledge'), join(target, 'knowledge'))

