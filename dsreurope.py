import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set the plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')

# CSV Loading
from pathlib import Path

def auto_load_and_profile():
    """Find all CSVs in data/ and profile them."""
    data_dir = Path("data")
    csv_files = sorted(data_dir.glob("*.csv"))
    
    if not csv_files:
        print("No CSV files found in data/ directory.")
        print("Make sure your Kaggle files are extracted there.")
        return
    
    print(f"Found {len(csv_files)} CSV file(s):\n")
    
    for path in csv_files:
        name = path.stem
        print(f"\n{'='*60}")
        print(f"DATASET: {name}")
        print(f"{'='*60}")
        
        try:
            df = pd.read_csv(path)
            print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
            print(f"\nColumns:\n{df.dtypes.to_string()}")
            print(f"\nMissing values: {df.isnull().sum().sum():,} total ({df.isnull().sum().sum() / (df.shape[0]*df.shape[1]):.1%})")
            print(f"\nDuplicated rows: {df.duplicated().sum():,}")
            
            # Show first few column names for reference
            print(f"\nColumn list: {list(df.columns[:10])}{'...' if len(df.columns) > 10 else ''}")
            
        except Exception as e:
            print(f"ERROR loading {name}: {e}")
    
    return

# RUN IT
auto_load_and_profile()

