import tables as tb
import pandas as pd

from os.path import expandvars, basename

def explore_file(filename):
    filename = expandvars(filename)
    with tb.open_file(filename) as h5f:
        print(h5f)


def read_table(filename, path):
    "Real the full table in :path: inside :filename:"
    filename = expandvars(filename)
    
    with tb.open_file(filename) as h5f:
        if not hasattr   (h5f.root, path) : raise LookupError(f"{path} not found in {basename(filename)}")
        table = h5f.root.__getattr__(path)
        if not isinstance(table, tb.Table): raise LookupError(f"{path} is not a table in {basename(filename)}")
        try:
            df = pd.DataFrame.from_records(table.read())
        except ValueError:
            df = table.read()
    return df

