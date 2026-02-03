def clean_data(data):
    data = data.dropna()
    data = data.drop_duplicates()
    return data
