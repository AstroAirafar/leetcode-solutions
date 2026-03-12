import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    a = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset='salary')
    col = f'getNthHighestSalary({N})'
    if N > 0 and len(a) >= N:
        return pd.DataFrame({col : [a.iloc[N-1]['salary']]})
    else :
        return pd.DataFrame({col : [None]})