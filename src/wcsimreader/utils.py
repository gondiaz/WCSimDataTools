import tables as tb
import pandas as pd


def explore_file(filename):
    with tb.open_file(filename) as h5f:
        print(h5f)


def read_table(filename, path):
    "Real the full table in :path: inside :filename:"
    
    with tb.open_file(filename) as h5f:
        table = h5f.root.__getattr__(path)
        if not hasattr   (h5f.root, path) : raise Exception(":path: not found in :filename:")
        if not isinstance(table, tb.Table): raise Exception(":path: is not a table in :filename:")

        if table.nrows == 1:
            sets    = table.read()
            indexes = sets.dtype.fields.keys()
            df = pd.DataFrame(index=indexes, columns=["values"])
            for index in indexes:
                df.loc[index, "values"] = sets[index][0]
        elif table.nrows > 1:
            df = pd.DataFrame.from_records(table.read())
    return df

