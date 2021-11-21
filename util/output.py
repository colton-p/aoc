import collections
import os
import types

def smart_output(value):
    if type(value) == types.GeneratorType:
        value = list(value)

    if isinstance(value, collections.Iterable):
        if all(type(v) == str and len(v) == 1 for v in value):
            return ''.join(value)

    
    return value

def to_clipboard(value):
    return os.system(f'echo "{value}" | tr -d "\n" | pbcopy')

def pretty_answer(label, value):
    raw = f"{value}"
    smart = smart_output(value)

    print(label, smart)
    if smart != value:
        print('  raw:', raw)
    if smart is not None:
        to_clipboard(smart)