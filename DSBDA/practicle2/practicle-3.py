import pandas as pd
df=pd.read_csv(r"D:\DSBDA practicles\Salary_Data.csv")
data=pd.read_csv(r"D:\DSBDA practicles\Iris.csv")
#OPERATION-1
#print(df)
print(df.groupby(['Age'])['Salary'].mean())


#group by
#OPERATION-2

irisset=(data['Species']=='Iris-setosa')
print('Iris-setosa')
print(data[irisset].describe())

irisver=(data['Species']=='Iris-versicolor')
print('Iris-versicolor')
print(data[irisver].describe())

irisvir=(data['Species']=='Iris-virginica')
print('Iris-virginica')
print(data[irisvir].describe())
#for mean
data.mean()

data.loc[:,'Id'].mean()

data.mean(axis=0)[0:4] 
data.mean(axis=1)[0:4]
data.iloc[0:4].mean()

#for median

data.median()
data.loc[:,'SepalLengthCm'].median()
data.median(axis=1)[0:2]
data.median(axis=0)[0:2]
data.iloc[0:3].median()

# for mode
#print(data.mode())
#print(data.loc[:,'SepalLengthCm'].mode())

#for minimum 
print(data.min())
print(data.loc[:,'Id'].min(axis=0,skipna=False))

# for maximum
print(data.max())
print(data.loc[:,'Id'].max(axis=0,skipna=False))

#for standard deviation
print(data.std())
print(data.loc[:,'Id'].std())
print(data.std(axis=1)[0:4])

