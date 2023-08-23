import pandas as pd
import smartsheet

# Smartsheet API access token
SMARTSHEET_ACCESS_TOKEN = 'your_smartsheet_access_token'
# Smartsheet ID
SMARTSHEET_ID = 'your_smartsheet_id'

def get_smartsheet_data():
    smartsheet_client = smartsheet.Smartsheet(SMARTSHEET_ACCESS_TOKEN)
    sheet = smartsheet_client.Sheets.get_sheet(SMARTSHEET_ID)

    data = []
    for row in sheet.rows:
        row_data = {}
        for cell in row.cells:
            row_data[cell.column_id] = cell.value
        data.append(row_data)

    df = pd.DataFrame(data)
    return df
