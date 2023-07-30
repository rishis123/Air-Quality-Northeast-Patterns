import pandas as pd

for i in range(0,9):
    df = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_200" + str(i) + ".zip")

    df.head()

    new_df = df[(df["State Code"] == 9) | (df["State Code"] == 23) | (df["State Code"] == 25) | (df["State Code"] == 33) | (df["State Code"] == 34) | (df["State Code"] == 36) | (
        df["State Code"] == 42) | (df["State Code"] == 44) | (df["State Code"] == "50")][['State Code', 'Parameter Name', 'Arithmetic Mean']]

    new_df_1 = new_df[(new_df["Parameter Name"] == "Ozone") | (new_df["Parameter Name"] == "Sulfur dioxide") | (
        new_df["Parameter Name"] == "Carbon monoxide") | (new_df["Parameter Name"] == "Nitrogen dioxide (NO2)")]

    new_df_1.to_excel('extracted_data_200' + str(i) +'.xlsx', index=None, header=True)

for i in range(10,22):
    df = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_20" + str(i) + ".zip")

    df.head()

    new_df = df[(df["State Code"] == 9) | (df["State Code"] == 23) | (df["State Code"] == 25) | (df["State Code"] == 33) | (df["State Code"] == 34) | (df["State Code"] == 36) | (
        df["State Code"] == 42) | (df["State Code"] == 44) | (df["State Code"] == "50")][['State Code', 'Parameter Name', 'Arithmetic Mean']]

    new_df_1 = new_df[(new_df["Parameter Name"] == "Ozone") | (new_df["Parameter Name"] == "Sulfur dioxide") | (
        new_df["Parameter Name"] == "Carbon monoxide") | (new_df["Parameter Name"] == "Nitrogen dioxide (NO2)")]

    new_df_1.to_excel('extracted_data_20' + str(i) +'.xlsx', index=None, header=True)
