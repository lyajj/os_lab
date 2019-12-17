from os import path

def not_exist_guard(f):
    def decorator(*args, **kwargs):
        args = args[0]
        if len(args) != 1:
            return 'Invalid args length'
        pathname = args[0]
        filepath = path.abspath(pathname)
        if path.exists(filepath) and path.isfile(filepath):
            f(filepath)
        else:
            return 'File does not exist!'
    return decorator


def exist_guard(f):
    def decorator(*args, **kwargs):
        args = args[0]
        if len(args) != 1:
            print('Invalid args length')
            return
        pathname = args[0]
        filepath = path.abspath(pathname)
        if path.exists(filepath) and path.isfile(filepath):
            print('File already exists!')
            return
        else:
            f(filepath)
    return decorator
