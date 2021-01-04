import pandas as pd
filename ="data_csv.csv"
data = pd.read_csv(filename)
data = data.fillna('NA')
dic = {}
for index,rows in data.iterrows():
    dic[rows.Code] = rows.Name
sorted_tuple = sorted(dic.items(), key = lambda kv: kv[0])
sorted_dic = dict(sorted_tuple)
code1 = input("Enter country code 1: ")
code2 = input("Enter country code 2: ")
if code1 > code2:
    code1, code2 = code2, code1
for k,v in sorted_dic.items():
    if k > code1 and k < code2:
        print(v)
    
   
