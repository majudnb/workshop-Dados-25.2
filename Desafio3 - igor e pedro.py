import numpy as np
import random

dias = np.array (["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"])

temperaturas = [random.randint(20, 35) for _ in range(7)]

print('Dias: ', dias)
print('Temperatura:', temperaturas)
print()

import pandas as pd

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
temperatura2 = (temperaturas)

df = pd.DataFrame({"Dia": dias, "Temp": temperaturas})

print(df)
print(df["Temp"].mean())
print()

import matplotlib.pyplot as plt

x = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
y = (temperaturas)

plt.plot(x, y, color = 'Red')
plt.xlabel('Dias')
plt.ylabel('Temperatura')
plt.title('Variação de temperatura')
plt.legend()
plt.show()
