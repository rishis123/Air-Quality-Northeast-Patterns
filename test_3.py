import pandas as pd

df = pd.read_excel('extracted_data_2000.xlsx')

df.head()

arr = [9, 23, 25, 33, 34, 36, 42, 44, 50]

arr1 = ['Carbon monoxide', 'Ozone', 'Sulfur dioxide', 'Nitrogen dioxide (NO2)']

arr2 = []

for i in arr:
    for j in arr1:
        new_df = df[(df["State Code"] == i) & (df['Parameter Name'] == j)]
        arr2.append(new_df["Arithmetic Mean"].mean())
        
#x = pd.DataFrame({"State Names":arr})
#y = pd.DataFrame({"Gases": arr1})
#z = pd.DataFrame({"Means": arr2})

#x = pd.concat([x,y])
#x = pd.concat([x,z])

#print(x)
#x.to_excel('Output.xlsx')