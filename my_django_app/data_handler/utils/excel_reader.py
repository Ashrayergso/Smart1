```python
import pandas as pd

def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error occurred while reading the excel file: {e}")
        return None
```