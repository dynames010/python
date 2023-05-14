import pandas as pd
df = pd.read_csv(r"D:\xzc\学习\python库\pandas_test.csv",names=['a','b','c','d'],header=0,skiprows=2)
data = {'Name': ['Smith', 'Parker'], 'ID': [101, 102], 'Language': ['Python', 'JavaScript']}
df = pd.DataFrame(data)
print('DataFrame valures:\n',df)
csv_data = df.to_csv()
print(csv_data)
print(df)

excel_info = pd.DataFrame({'name':['a','b'],'rank':['1','2'],'subjext':['test','math']},index=['name1','name2'])
writer = pd.ExcelWriter('test.xlsx')
excel_info.to_excel(writer)
writer.save()