import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    a = employee.groupby('managerId').size()
    return employee[employee['id'].isin(a[a >=5].index)][['name']]