import pandas as pd
data={
    'Name':['prajakta','pranoti','shweta','mansi','rutuja'],
    'marks':[90,80,70,60,50],
    'age':[20,21,19,20,20]
}
df=pd.DataFrame(data)
'''for i, j in df.iterrows():
    print(i, j)
    print()'''
col= ['Name']
print(df[col].head(2))
print(df[col].tail(2))

print(df['marks'].mean())



