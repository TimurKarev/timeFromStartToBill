from datetime import datetime
import pandas as pd
from utils.clean import clean_multiple_rows
from pathlib import Path
import os

def clean_1c_exel(file_name='C_data.xls'):
    with open(Path.cwd() / 'data' / file_name, "rb") as f:
        df = pd.read_excel(f, header=None)
    df = df.fillna(0)

    df = df.drop(columns=[1,3,4])

    head_ind, head_nam = get_order_headers(df)

    orders_number = len(head_ind)
    df_list = [None] * (orders_number)
    for i, index in enumerate(head_ind):
        if (i+1) >= orders_number:
            df_list[i] = df.iloc[index + 1: -1]
        else:
            df_list[i] = df.iloc[index+1: head_ind[i+1]]
            d = df_list[i]
        df_list[i]['order_number'] = head_nam[i]

    return df_list
    # mask = df[0].str.find('Заказ на производство ЭТИ0000') == 0
    # header_indexes = mask[mask].index.tolist()
    #
    # order_num_list = []
    # for it in header_indexes:
    #     for word in df.iloc[it, 0].split():
    #         if 'ЭТИ0000' in word:
    #             order_num_list.append(word[-4:])
    #             break
    #
    # df_order_list = []
    # len_hi = len(header_indexes)
    # for index, item in enumerate(header_indexes):
    #     if index + 1 > len_hi:
    #         df_order_list.append(df.iloc[item:header_indexes[index]])
    #     else:
    #         df_order_list.append(df.iloc[item:])
    #
    # df_order_list1 = []
    # for index, df_order_item in enumerate(df_order_list):
    #     df_order_item = df_order_item.drop(columns=[1, 3, 4])
    #     df_order_item = df_order_item.fillna(0)
    #     df_order_item = df_order_item[
    #         (df_order_item[5] != 0) & \
    #         (df_order_item[6] != 0) & \
    #         (df_order_item[7] != 0) & \
    #         (df_order_item[8] != 0) & \
    #         (df_order_item[9] != 0)
    #         ]
    #     mapper = {
    #         0: 'part_name',
    #         2: 'initial_date',
    #         5: 'creation_date',
    #         6: 'approved_date',
    #         7: 'master_name',
    #         8: 'manager_name',
    #         9: 'bill_date',
    #     }
    #     df_order_item = df_order_item.rename(columns=mapper)
    #     df_order_item['num_order'] = order_num_list[index]
    #     #print(df_order_item)
    #     df_order_list1.append(df_order_item)
    #
    # #print(order_num_list)
    # clean_df = pd.DataFrame()
    # for index, df_order_item in enumerate(df_order_list1):
    #     l = df_order_item.apply(clean_multiple_rows, axis=1)
    #     for i in l:
    #         clean_df = clean_df.append(i, ignore_index=True)
    #     #clean_df['order_num'] = order_num_list[index]
    #
    # with open(Path.cwd() / 'data' / 'output1.csv', "w") as f:
    #     clean_df.to_csv(f, encoding="windows-1251")
    #
    # return clean_df
def get_order_headers(df: pd.DataFrame,
                      row_pattern='Заказ на производство ЭТИ0000',
                      word_pattern='ЭТИ0000'):

    mask = df[0].str.find('Заказ на производство ЭТИ0000') == 0
    header_ind = mask[mask].index

    ind_list = []
    ord_list = []
    for index in header_ind:
        string_list = df.iloc[index, 0].split()
        for i, word in enumerate(string_list):
            if 'ЭТИ0000' in word:
                ind_list.append(index)
                ord_list.append(word[-4:])

    return ind_list, ord_list