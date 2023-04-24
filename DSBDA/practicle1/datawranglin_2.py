
import pandas as pd	
from sklearn import preprocessing
data = pd.read_csv(r"D:\DSBDA practicles\practicle1\employees.csv.xls")
print(data.info())


#check for null values in dataset
print(data.isnull().sum())
#print the all 	 column with null value
data[data.isnull().any(axis=1)]
#Create dummy NaN value on 2 cells
data.iloc[2,1]=None
data.iloc[5,0]=None
data.iloc[:, 0].values
data.head(2)
data.iloc[:, 1].values
#groupby count of missimg values
print(data.groupby(['Gender'])['Team'].apply(lambda x:x.isnull().sum()))

#method to change data tyape
data.select_dtypes(include='int64')

data["Salary"]=data["Salary"].astype(bool)

data["Salary"]= data["Salary"].apply(lambda x: bool(x))
print(data) 

# formatting and normalization
 
min_max_scaler=preprocessing.normalize(data)

print(min_max_scaler)
x_scaled=min_max_scaler.fit_transform(x)

data_normalized=pd.DataFrame(x_scaled)
print(data_normalized)
