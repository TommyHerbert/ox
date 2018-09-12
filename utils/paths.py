from os.path import sep, normpath


def to_package_path(dir_path, final_dot=False):
    if dir_path == '':
        return dir_path
    package_path = normpath(dir_path).replace(sep, '.')
    return package_path + '.' if final_dot else package_path

