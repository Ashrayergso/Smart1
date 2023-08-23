import pandas as pd

def compare_data(smartsheet_df, excel_df):
    # Find common columns between the two dataframes
    common_columns = smartsheet_df.columns.intersection(excel_df.columns)

    # Filter the dataframes to only include the common columns
    smartsheet_df = smartsheet_df[common_columns]
    excel_df = excel_df[common_columns]

    # Merge the two dataframes on the common columns
    merged_df = pd.merge(smartsheet_df, excel_df, on=list(common_columns), how='outer', indicator=True)

    # Find rows that exist in both dataframes (matches), in the smartsheet only, and in the excel only
    matches = merged_df[merged_df['_merge'] == 'both']
    smartsheet_only = merged_df[merged_df['_merge'] == 'left_only']
    excel_only = merged_df[merged_df['_merge'] == 'right_only']

    # For rows that exist in both dataframes, check if 'name', 'sign on date', and 'sign off date' are the same
    matches['is_same'] = matches.apply(lambda row: row['name_x'] == row['name_y'] and row['sign on date_x'] == row['sign on date_y'] and row['sign off date_x'] == row['sign off date_y'], axis=1)

    # Separate matches into rows that are the same and rows that are different
    same_rows = matches[matches['is_same'] == True]
    different_rows = matches[matches['is_same'] == False]

    return same_rows, different_rows, smartsheet_only, excel_only
