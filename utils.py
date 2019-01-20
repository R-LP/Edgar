import os
import pandas as pd

def load_folder_csv(folder, prefix=None, sep=",",encoding="utf-8"):
    files = os.listdir(folder)
    if prefix is not None:
        files = [f for f in files if f.startswith(prefix)]
        
    dfs = []
    for f in files:
        in_p = os.path.join(folder, f)
        df = pd.read_csv(in_p, sep=sep, encoding=encoding)
        dfs.append(df)
        
    return pd.concat(dfs, ignore_index=True)