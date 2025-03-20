def filter_dataframe(dataframe, start_date, end_date):
    """
    Filters a DataFrame to include only rows within the specified date range.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame that includes a "Date" column to be used for filtering.
        start_date (str): The beginning date of the range. The row with this date will be included.
        end_date (str): The ending date of the range. The row with this date will be included.

    Returns:
        pandas.DataFrame: A DataFrame containing only the rows between start_date and end_date.
    """
    dataframe.set_index("Date", inplace=True)
    
    return dataframe.loc[start_date:end_date]
