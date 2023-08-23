from django.shortcuts import render
from .utils import smartsheet_api, excel_reader, data_comparer, data_updater

def index(request):
    return render(request, 'data_handler/index.html')

def process_data(request):
    # Connect to Smartsheet API and retrieve data
    smartsheet_df = smartsheet_api.get_data()

    # Read local excel file and store its data
    excel_df = excel_reader.read_excel()

    # Compare the data from the Smartsheet DataFrame with the Excel DataFrame
    comparison_result = data_comparer.compare_data(smartsheet_df, excel_df)

    # Update the Smartsheet DataFrame to match the Excel DataFrame
    updated_smartsheet_df = data_updater.update_data(smartsheet_df, comparison_result)

    # Write the updated Smartsheet DataFrame back to the Smartsheet
    smartsheet_api.write_data(updated_smartsheet_df)

    context = {
        'excel_data': excel_df.to_html(),
        'smartsheet_data': smartsheet_df.to_html(),
        'updated_data': updated_smartsheet_df.to_html(),
    }

    return render(request, 'data_handler/result.html', context)

def result(request):
    # TODO: Implement the functionality for the result view
    pass
