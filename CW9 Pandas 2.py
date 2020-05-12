import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
#Zad 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
x = df.groupby(["Rok"]).agg({"Liczba": ['count']})
wykres = x.plot()
wykres.set_ylabel('Rok')
wykres.set_xlabel('Liczba')
wykres.legend()
plt.title('Liczba urodzonych dzieci dla kazdego roku')
plt.show()
#Zad 2
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
l = df.groupby(['Plec']).agg({"Liczba": ['sum']})
wykres = l.plot.bar()
wykres.legend()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Płeć')
plt.title('Suma urodzonych dzieci lata 2000-2017 z podziałem na płeć')
plt.show()
#Zad 3
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
x = (df[((df.Rok >= 2013) & (df.Rok <= 2017))].groupby(['Plec']).agg({'Liczba': ['sum']}))
wykres = x.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title("Suma urodzonych dzieci  lata 2013-2017 z podziałem na płeć")
plt.show()
#Zad 4 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
a = ['sepal-width']
b = ['petal-width']
dataset = pd.read_csv(url, names='names')
colors = np.random.rand(1)
plt.scatter(a,b,c=colors)
plt.show()
#Zad 5
df = pd.read_csv('zamowienia.csv',sep=";")
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = grupa.plot.bar()
wykres.legend()
wykres.set_ylabel('Zamowienia')
wykres.set_xlabel('Sprzedawca')
plt.title(' ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.show()