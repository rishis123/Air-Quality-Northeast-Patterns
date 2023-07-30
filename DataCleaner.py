import pandas as pd

arr = [9, 23, 25, 33, 34, 36, 42, 44, 50]

arr1 = ['Carbon monoxide', 'Ozone', 'Sulfur dioxide', 'Nitrogen dioxide (NO2)']

for k in range(0,10):
    df = pd.read_excel('extracted_data_200' + str(k) + '.xlsx')

    df.head()

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

    data.to_excel('extracted_data_200' + str(k) + '.xlsx')
    print(k)

for k in range(10,23):
    df = pd.read_excel('extracted_data_20' + str(k) + '.xlsx')

    df.head()

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

    data.to_excel('extracted_data_20' + str(k) + '.xlsx')
    print(k)
