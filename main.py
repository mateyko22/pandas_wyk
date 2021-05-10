import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# s = pd.Series(np.random.randn(1000), pd.date_range('01/01/2015', periods=1000))
#
# s = s.cumsum()
# print(s)
# s.plot()
# plt.show()

# data = {"Kraj": ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         "Stolica": ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         "Kontynent": ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         "Populacja": [121510512, 516815181, 121510115, 15133222]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
#
# print(grupa)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Populacja')
# wykres.set_ylabel('Mld')
#
# plt.xticks(rotation=0)
# plt.title('Populacja z podzialem na kontynenty')
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
#
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0,0))
# plt.legend(loc='lower right')
# plt.title('Suma zamówień dla sprzedawcy')
# plt.show()


# Zad 1
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Rok'])['Liczba dzieci'].sum()
# grupa.plot()
# plt.title('Suma urodzonych dzieci w danym roku')
# plt.legend(loc='lower right')
# plt.show()


# Zad 2
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Plec'])['Liczba'].sum()
#
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Liczba dzieci')
# wykres.set_xlabel('Płeć')
# plt.show()

# Zad 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
#
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.where(df['Rok'] > 2012).groupby(['Plec'])['Liczba'].sum()
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0,0))
#
# plt.title('Ilość urodzonych chłopców i dziewczynek')
# plt.show()

# Zad 4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców
# (zbiór danych zamówienia.csv).

# df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
#
# grupa = df.groupby(['Sprzedawca'])['idZamowienia'].sum()
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Sprzedawca')
# wykres.set_ylabel('Liczba zamówień')
# plt.show()

# plt.plot([1, 2, 3, 4])
# plt.ylabel('Przyklad')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
#
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='postać liniowa')
# plt.plot(x, x**2, label='postać kwadratowa')
# plt.plot(x, x**3, label='postać sześcienna')
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
#
# plt.title('Przykladowe wykresy')
# plt.legend()
# plt.show()

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
#
# plt.plot(x, s, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.title('Wykres sin(x)')
# plt.legend()
# plt.show()
