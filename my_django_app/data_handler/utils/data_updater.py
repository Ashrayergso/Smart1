import pandas as pd
from .smartsheet_api import get_smartsheet_df, update_smartsheet
from .data_comparer import compare_dataframes

def update_data(excel_df):
    smartsheet_df = get_smartsheet_df()

    # Compare the dataframes and get the updated dataframe
    updated_df = compare_dataframes(smartsheet_df, excel_df)

    # Update the smartsheet with the updated dataframe
    update_smartsheet(updated_df)

def compare_dataframes(smartsheet_df, excel_df):
    # Merge the dataframes on 'name', 'sign on date', and 'sign off date'
    merged_df = pd.merge(smartsheet_df, excel_df, on=['name', 'sign on date', 'sign off date'], how='outer')

    # For each column that exists in both dataframes, update the smartsheet dataframe to match the excel dataframe
    for column in merged_df.columns:
        if column in smartsheet_df.columns and column in excel_df.columns:
            merged_df[column] = merged_df[column + '_y'].combine_first(merged_df[column + '_x'])

    # Drop the duplicate columns
    merged_df = merged_df.loc[:,~merged_df.columns.duplicated()]

    return merged_df
