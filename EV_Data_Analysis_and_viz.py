import pandas as pd

file = r'C:\\Users\\jschu\\Desktop\\Coding Stuff\\Battery_Model\\EV_Data\\TripA01.csv'

df1 = pd.read_csv(file,sep=';',encoding='ISO-8859-1')
print(df1.head())