import builtins
import string

BUILTINS_DATA = {
    'io' : [
        print, input, open, ],
    'introspection' : [
        dir, type, id,
        isinstance, callable,
        help, issubclass, len, vars, ],
    'types' : [
        object, type, 
        int, bool, float, complex,
        str, bytes,
        tuple, list,
        frozenset, set,
        dict, ],
    'iteration' : [
        range, enumerate, zip,
        map, filter, # we really don't use these two, prefer list comprehensi
        iter, next,
        slice, reversed, ],
    'OOP' : [
        staticmethod, classmethod,
        property,
        delattr, setattr, getattr, ],
    'Math' : [
        abs, all, any, bin,
        hex, oct, pow, round,
        sum, ]
}

def list_builtins():
    """This lists all the builtins"""
    return [n for n in dir(builtins) if n[0] in string.ascii_lowercase]

def api(obj):
    """list the application programming interface of an object"""
    return [n for n in dir(obj) if n[0] != '_']

def create_obscured_doc(obj, name):
    """Wgiven an object with a name, returns the obscured documentation"""
    return obj.__doc__.replace(name, '*' * len(name))
