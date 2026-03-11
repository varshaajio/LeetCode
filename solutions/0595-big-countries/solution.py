import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # 1. Filter rows where area is >= 3,000,000 OR population is >= 25,000,000
    is_big = (world['area'] >= 3000000) | (world['population'] >= 25000000)
    
    # 2. Select only the required columns: name, population, and area
    return world.loc[is_big, ['name', 'population', 'area']]
