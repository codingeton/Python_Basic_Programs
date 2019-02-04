import pandas as pd

Data  = [1,2,3,4,5]
#Creating series with different index values. s prints the data with default index
s = pd.Series(Data)
#Predefined index values
Index = ['a','b','c','d','e']
#Creating series with Predefined index values. si prints the data with the custom index
si = pd.Series(Data, Index)
print(si)
