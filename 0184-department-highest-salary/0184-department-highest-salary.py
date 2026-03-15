import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    max_salary = df.groupby('name_dept')['salary'].transform('max')
    result = df[df['salary'] == max_salary]
    return result[['name_dept', 'name_emp', 'salary']].rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })