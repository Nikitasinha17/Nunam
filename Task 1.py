import pandas as pd
#defining sheets 
sheets = []
x = pd.ExcelFile('data.xs')
for sn in x.sheet_names:
    if 'Detail_67_' in sn:
        sheets.append(sn)
df = []
#looping the list of sheets 
for i in sheets:
    df.append(pd.read_excel('data.xs', sheet_name = i))
#concatinate the data list into dataframe
df_final = pd.concat(df)
#write the dataframe to the csv file
df_final.to_csv('detail.csv')
print("Successfully created.")


sheets = []
x = pd.ExcelFile('data.xls')
for sn in x.sheet_names:
    if 'DetailVol_67_' in sn:
        sheets.append(sn)
df = []
#looping through the list of sheets 
for i in sheets:
    df.append(pd.read_excel('data.xs', sheet_name = i))
#concating the data list into dataframe
df_final = pd.concat(df)
#writing the dataframe to the csv file
df_final.to_csv('detailVol.csv')
print("Successfully created.")


sheet1 = []
x1 = pd.ExcelFile('data.xs')
for sn in x1.sheet_names:
    if 'DetailTemp_67_' in sn:
        sheet1.append(sn)

sheet2 = []
x2 = pd.ExcelFile('data_1.xs')
for sn in x2.sheet_names:
    if 'DetailTemp_67_' in sn:
        sheet2.append(sn)
df = []
#looping through the list of sheets
for i in sheet1:
    df.append(pd.read_excel('data.xs', sheet_name = i))
for i in sheet2:
    df.append(pd.read_excel('data_1.xs', sheet_name = i))
    
#concating the data list into dataframe
df_final = pd.concat(df)
#writing the dataframe to the csv file
df_final.to_csv('detailTemp.csv')
print("Successfully created.")
