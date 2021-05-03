import pandas as pd

sheets = pd.read_excel("data.xlsx", sheet_name=None)
sheets2 = pd.read_excel("data_1.xlsx", sheet_name=None)


detail = pd.DataFrame()
detailVol = pd.DataFrame()
detailTemp = pd.DataFrame()


for i in sheets.keys():
    if('Detail_67_' in i):
        temp = sheets[i]
        detail = pd.concat([details, df])
    elif('DetailVol_67_' in i):
        temp2 = sheets[i]
        detailVol = pd.concat([detailVol, df2])
    elif('DetailTemp_67_' in i):
        temp3 = sheets[i]
        detailTemp = pd.concat([detailTemp, df3])

for i in sheets2.keys():
    if('Detail_67_' in i):
        temp = sheets2[i]
        detail = pd.concat([details, df])
    elif('DetailVol_67_' in i):
        temp2 = sheets2[i]
        detailVol = pd.concat([detailVol, df2])
    elif('DetailTemp_67_' in i):
        temp3 = sheets2[i]
        detailTemp = pd.concat([detailTemp, df3])

detail.to_csv('detail.csv')
detailVol.to_csv('detailVol.csv')
detailTemp.to_csv('detailTemp.csv')
