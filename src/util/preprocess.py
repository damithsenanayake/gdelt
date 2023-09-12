import numpy as np
import pandas as pd

def strip_names(string_list):
    name_count_list = string_list.split(";")
    offsets = list(map(lambda x: int(x.split(',')[1]), name_count_list))
    names = list(map(lambda x: str(x.split(',')[0]), name_count_list))

    offsets_order = np.argsort(offsets)

    names_ordered = np.array(names)[offsets_order]

    indexes = np.unique(names_ordered, return_index=True)[1]

    return [names_ordered[index] for index in sorted(indexes)]

def get_connectivity(dataframe):

    person_array = dataframe.V2Persons.values

    print(f' n(entries) = {len(person_array)}')
    connection_df = pd.DataFrame({'Source': pd.Series(dtype='str'), 'Target': pd.Series(dtype='str')})
    for d, p in enumerate(person_array):
        print(f'\r{d}/{len(person_array)}', end='')
        names = strip_names(p)
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                new_row = {'Source': names[i], 'Target': names[j]}
                connection_df = pd.concat([connection_df, pd.DataFrame(new_row, index=[0])], ignore_index = True)

    return connection_df
