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


