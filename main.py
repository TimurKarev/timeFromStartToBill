from datetime import datetime
import pandas as pd
from utils.clean import clean_multiple_rows
from  pathlib import Path
import os


def clean_1c_exel(file_name):
    dir_path = Path.cwd()

    #TODO переделать в path
    df = pd.read_excel(
        Path.cwd() / 'data' / file_name,
        header=None
    )

    mask = df[0].str.find('Заказ на производство ЭТИ0000') == 0
    header_indexes = mask[mask].index.tolist()

    #df = df.iloc[header_indexes[0]:header_indexes[1]]
    df_order_list = []
    len_hi = len(header_indexes)
    for index, item in enumerate(header_indexes):
        if index + 1 > len_hi:
            df_order_list.append(df.iloc[item:header_indexes[index]])
        else:
            df_order_list.append(df.iloc[item:])

    df_order_list1 = []
    for df_order_item in df_order_list:
        df_order_item = df_order_item.drop(columns=[1, 3, 4])
        df_order_item = df_order_item.fillna(0)
        df_order_item = df_order_item[
            (df_order_item[5] != 0) & \
            (df_order_item[6] != 0) & \
            (df_order_item[7] != 0) & \
            (df_order_item[8] != 0) & \
            (df_order_item[9] != 0)
            ]
        mapper = {
            0: 'part_name',
            2: 'initial_date',
            5: 'creation_date',
            6: 'approved_date',
            7: 'master_name',
            8: 'manager_name',
            9: 'bill_date',
        }
        df_order_item = df_order_item.rename(columns=mapper)
        df_order_list1.append(df_order_item)

    return df_order_list1
