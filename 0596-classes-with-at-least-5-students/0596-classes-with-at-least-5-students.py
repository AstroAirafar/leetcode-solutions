import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    a = courses.groupby('class').size()
    return courses[courses['class'].isin(a[a>=5].index)][['class']].drop_duplicates()