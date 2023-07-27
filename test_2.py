import pandas as pd

df = pd.read_csv("test.csv")

df.head()

new_df = df[(df["State Code"] == 9) | (df["State Code"] == 23) | (df["State Code"] == 25) | (df["State Code"] == 33) | (df["State Code"] == 34) | (df["State Code"] == 36) | (
    df["State Code"] == 42) | (df["State Code"] == 44) | (df["State Code"] == "50")][['State Code', 'Parameter Name', 'Arithmetic Mean', 'Arithmetic Standard Dev']]

new_df_1 = new_df[(new_df["Parameter Name"] == "Ozone") | (new_df["Parameter Name"] == "Sulfur dioxide") | (
    new_df["Parameter Name"] == "Carbon monoxide") | (new_df["Parameter Name"] == "Nitrogen dioxide (NO2)")]

print(new_df_1)
new_df_1.to_excel('extracted_data_2000.xlsx', index=None, header=True)
