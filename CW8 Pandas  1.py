#Zad 1
import pandas as pd
import xlrd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)
#Zad 2a
print(df[df['Liczba']>1000])
#Zad 2b
print(df[df['Imie'] == 'Krystian'])
#Zad 2c
print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
#Zad 2d
print(df[df['Rok'] <= 2005].agg({'Liczba': ['sum']}))
#Zad 2e
print(df[df['Plec'] == "M"].agg({'Liczba': ['sum']}))
print(df[df['Plec'] == "K"].agg({'Liczba': ['sum']}))
#Zad 2f
print(df.sort_values('Liczba', ascending=False).groupby( ['Rok', 'Plec']).nth(0))
#Zad 2g
print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values( ('Liczba', 'sum'), ascending=False).iloc[[0, 1]])
#Zad 3
df = pd.read_csv('zamowienia.csv')
#Zad 3a
print(df['Sprzedawca'].unique())
#zad 3b
print(df['Utarg'].nlargest(5))
#Zad 3c
print(df.groupby('Sprzedawca')['Sprzedawca'].count())
#Zad 3d
print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))
#Zad 3e
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '01-01-2005')  & (df['Data zamowienia'] <= '31-12-2005')].agg({'Utarg': ['sum']}))
#Zad 3f
print(df['Utarg'][(df['Data zamowienia'] >= '01-01-2004') & (df['Data zamowienia'] <= '31-12-2004')].mean())
#Zad 3g
df2004 = df[(df['Data zamowienia'] >= '01-01-2004') &
            (df['Data zamowienia'] <= '31-12-2004')]
df2004.to_csv(
    'D:\wizualizacja\zamówienia_2004.csv')
df2005 = df[(df['Data zamowienia'] >= '01-01-2005') &
            (df['Data zamowienia'] <= '31-12-2005')]
df2005.to_csv(
    'D:\wizualizacja\zamówienia_2005.csv')
               
  

