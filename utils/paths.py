from os.path import sep

def to_package_path(directory_path):
    return directory_path.replace(sep, '.')
