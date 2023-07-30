import pandas as pd #This program cleans the data from the original data-extracter, including taking arithmetic means (if numerous datapoints in a single year, single gas, and single state). 

df = pd.read_excel('extracted_data_2000.xlsx')

df.head()

arr = [9, 23, 25, 33, 34, 36, 42, 44, 50]

arr1 = ['Carbon monoxide', 'Ozone', 'Sulfur dioxide', 'Nitrogen dioxide (NO2)']

arr2 = []

arr3 = []

arr4 = []

for i in arr:
    for j in arr1:
        new_df = df[(df["State Code"] == i) & (df['Parameter Name'] == j)]
        arr2.append(new_df["Arithmetic Mean"].mean())
        arr3.append(j)
        arr4.append(i)

data = pd.DataFrame({
    'State Names': arr4,
    'Gases': arr3,
    'Mean Value': arr2
})

data.to_excel('Output.xlsx')
