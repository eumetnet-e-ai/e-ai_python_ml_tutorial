from graphviz import Digraph
import inspect

def get_public_methods(cls):
    def is_local_method(m):
        return m.__qualname__.split('.')[0] == cls.__name__
    
    return {
        name for name, member in inspect.getmembers(cls)
        if (not name.startswith('_')
            and inspect.isfunction(member)
            and is_local_method(member))
    } 

def class_to_graphviz(cls, shortlist, dot=None, visited=None):
    dot = Digraph(format='svg', 
                 node_attr={'shape':'plaintext', 'style':'filled', 'fillcolor':'#f8f8f8'},
                 graph_attr={'rankdir':'LR'}) if not dot else dot
    visited = set() if visited is None else visited
    
    if cls in visited: 
        return dot
    visited.add(cls)
    
    # Get full class name with module path
    module = cls.__module__
    full_name = f"{module}.{cls.__name__}" if module != "__main__" else cls.__name__
    
    methods = get_public_methods(cls)
    if not "anemoi" in module:
        methods = methods & shortlist
    label = f'''<<table border="0" cellborder="0">
        <tr><td bgcolor="#e0e0e0"><font face="monospace"><b>{full_name}</b></font></td></tr>
        {"".join(f'<tr><td align="left">+ {m}()</td></tr>' for m in methods)}
    </table>>'''
    
    dot.node(str(id(cls)), label=label)
    
    for base in filter(lambda x: x.__name__ != 'object', cls.__bases__):
        class_to_graphviz(base, shortlist=shortlist, dot=dot, visited=visited)
        dot.edge(str(id(base)), str(id(cls)))
    
    return dot



def split_string(s):
    '''Split a string into a tuple of (string, int) if the string ends with an underscore followed by digits.'''
    parts = s.rsplit("_", 1)
    return (
        (parts[0], int(parts[1]))
        if len(parts) == 2 and parts[1].isdigit()
        else (s, None)
    )  
    
def get_class_name(obj):
    '''Get the class name of an object, including the module path if not built-in'''
    cls = obj.__class__
    return cls.__name__ if cls.__module__ == "builtins" else f"{cls.__module__}.{cls.__name__}"

def get_parent_class_name(obj):
    '''Get the parent class name of an object, including the module path if not built-in'''
    cls = obj.__class__.__bases__[0]
    return cls.__name__ if cls.__module__ == "builtins" else f"{cls.__module__}.{cls.__name__}"


import json, re

def generate_toc(notebook_path):
    '''Usage: generate_toc('aicon01.ipynb')'''
    with open(notebook_path) as f:
        nb = json.load(f)
    toc = []
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                m = re.match(r'^(#+)\s+(.*)', line)
                if m:
                    level = len(m.group(1))
                    title = m.group(2).strip()
                    anchor = title.lower().replace(' ', '-')
                    toc.append(f"{'  ' * (level-1)}- [{title}](#{anchor})")
    print('\n'.join(toc))


## Table styles for pandas DataFrames
pandas_table_style = [
    {'selector': 'th', 'props': [('text-align', 'left'), ('font-size', '16pt')]},  # headers
    {'selector': 'td', 'props': [('text-align', 'left'), ('font-size', '16pt')]}   # data cells
]


import re

def parse_shortname_def(filepath):
    """
    Parse a GRIB2 shortName.def file into a dict of dicts: {shortName: {key: value, ...}}.
    """
    d, lines, i = {}, open(filepath).readlines(), 0
    while i < len(lines):
        m = re.match(r"'(.+?)'\s*=\s*{", lines[i].strip())
        if m:
            sn, block = m.group(1), {}
            i += 1
            while i < len(lines) and lines[i].strip() != "}":
                m2 = re.match(r"(\w+)\s*=\s*([^;]+);", lines[i].strip())
                if m2:
                    k, v = m2.group(1), m2.group(2).strip()
                    block[k] = int(v) if v.isdigit() else v
                i += 1
            d[sn] = block
        i += 1
    return d

def parse_name_def(filepath):
    """
    Parse a block-style name.def file into a dict: {long_name: {key: value, ...}}.
    Ignores lines starting with '#'.
    """
    d, lines, i = {}, open(filepath).readlines(), 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#") or not line:
            i += 1; continue
        m = re.match(r"'(.+)' = \{", line)
        if m:
            long_name, block = m.group(1), {}
            i += 1
            while i < len(lines) and lines[i].strip() != "}":
                l2 = lines[i].strip()
                if l2 and not l2.startswith("#"):
                    m2 = re.match(r"(\w+)\s*=\s*([^;]+);", l2)
                    if m2:
                        k, v = m2.group(1), m2.group(2).strip()
                        block[k] = int(v) if v.isdigit() else v
                i += 1
            d[long_name] = block
        i += 1
    return d

def find_long_name_by_shortname(grib2_dict, shortname):
    """
    Return the key (long name) in name_dict whose value matches search_attrs exactly.
    """
    
    for shortname_dict, name_dict in grib2_dict:
        if shortname in shortname_dict:
            search_attrs = shortname_dict[shortname]
            for long_name, attrs in name_dict.items():
                if attrs == search_attrs:
                    return long_name            
    return None