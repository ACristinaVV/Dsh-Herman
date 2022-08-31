import pandas as pd
from typing import List, Optional


def get_data(path: str, col_names: Optional[List] = None, index: Optional[str] = None) -> pd.DataFrame:
    data = pd.read_csv(path, encoding='latin-1')
    if col_names:
        data = data[col_names]
    if index:
        data.set_index(index, inplace=True)
    return data
