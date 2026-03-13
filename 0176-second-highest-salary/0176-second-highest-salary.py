import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    a = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset='salary')
    col = f'SecondHighestSalary'
    if len(a)>1:
        return pd.DataFrame({col: [a.iloc[1]['salary']]})
    else:
        return pd.DataFrame({col: [None]})