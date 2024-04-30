import pandas as pd
import numpy as np
from multiprocessing import Pool, Process

from helpers import *


@timing
def get_unique_names_df():
    names = df ['name']
    # unique = names.drop_duplicates()
    unique = df.drop_duplicates(['name', 'university_name'])
    print(f'unique_names: {unique.count()}')


@timing
def get_unique_names_manually():
    unique_names = set()
    for record in dict_data:
        unique_names.add(record ['name'])
    print(f'unique_names: {len(unique_names)}')


if __name__ == '__main__':
    # LOADING DATA

    # print('Starting', flush=False)
    #
    # p = Pool(2)
    # p.apply_async(import_year)
    # p.apply_async(import_year_manually)
    # p.close()
    # p.join()

    # IMPORT
    # import_year()
    # dict_data = import_year_manually()
    #
    # dict_data = import_from_csv_manually()
    #
    # result_list = []
    # for value in dict_data:
    #     if value['university_name'] == 'ПНУ':
    #         result_list.append(value)
    #
    # students_count = 0
    # total_value = 0
    #
    # for student in result_list:
    #     students_count += 1
    #     total_value += float(student['zno_ukrainian'])
    #
    # average_value = total_value / float(students_count)
    # print(average_value)

    df = pd.read_csv('df_2020.csv',
                     dtype={
                         'zno_ukrainian': 'float64'
                     })

    result = df.query('university_name != "." and university_name != "-" and priority == "1"') \
        .groupby('university_name')[['zno_ukrainian', 'zno_math', 'zno_history']].count().reset_index()


    r = df.query('column_name.str.contains("АБ")', engine="python")
    print(result)

    result.to_excel('result.xlsx', index=False)
    #result.to_csv('result.csv')

    # result = df['university_name', 'name'].query(
    #     'university_name != "." and university_name != "." and zno_ukrainian > 190 and university_name != "ПНУ"'
    # ).count()
    #
    # print(result)





















    #df: DataFrame = import_df_from_csv()
    #dict_data = import_from_csv_manually()

    # get_unique_names_df()
    # get_unique_names_manually()
    # Get unique names
    # result = df.drop_duplicates(subset=['name', 'zno_ukrainian']).query(
    #     'zno_ukrainian > 0 and zno_math > 195 and priority == "1" and university_name != "."'
    # )
    # print(result)

    # result = df.query('university_name != "." and university_name != "-"')\
    #     .value_counts('university_name', sort=True, ascending=False)
    #
    # print(result.head(5).to_markdown())

    # result = df.query('university_name == "ЧНУ"')['zno_ukrainian'].mean()
    # print(result)

    #result = df.query('university_name != "." and university_name != "-"') \
    #    .groupby('university_name')[['zno_ukrainian', 'zno_math', 'zno_history']].mean()

    #print(result.head(10).to_markdown())
