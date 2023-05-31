import pandas as pd
from math import log

df = pd.read_csv('consoles.csv')

slc_mesa = 0; slc_portatil = 0; slc_hibrido = 0

for i in range(len(df)):
    coluna = df['tipo'][i]
    if coluna == 'console de mesa':
        slc_mesa += 1
    elif coluna == 'portatil':
        slc_portatil += 1
    elif coluna == 'hibrido':
        slc_hibrido += 1

total_1 = slc_mesa + slc_portatil + slc_hibrido
classes_tipo = 3; entropia_tipo = 0

count_tipo = [slc_mesa, slc_portatil, slc_hibrido]
prob_tipo = []

for i in range(0, classes_tipo):
    prob = count_tipo[i] / total_1
    prob_tipo.append(prob)

for i in range(0, classes_tipo):
    prob = prob_tipo[i]
    x = log(prob) / log(2)
    entropia_tipo += prob * x
    
print("\nEntropia de Consoles")
print("\nColuna 'TIPO'")
print("Entropia: {:.4}".format(entropia_tipo * -1))
print("Entropia Máxima: {:.4}".format(log(classes_tipo, 2)))

slc_sony = 0; slc_microsoft = 0; slc_nintendo = 0

for i in range(len(df)):
    coluna = df['fabricante'][i]
    if coluna == 'sony':
        slc_sony += 1
    elif coluna == 'microsoft':
        slc_microsoft += 1
    elif coluna == 'nintendo':
        slc_nintendo += 1

total_2 = slc_sony + slc_microsoft + slc_nintendo
classes_fabricante = 3; entropia_fabricante = 0

count_fabricante = [slc_sony, slc_microsoft, slc_nintendo]
prob_fabricante = []

for i in range(0, classes_fabricante):
    prob = count_fabricante[i] / total_2
    prob_fabricante.append(prob)

for i in range(0, classes_fabricante):
    prob = prob_fabricante[i]
    x = log(prob) / log(2)
    entropia_fabricante += prob * x

print("\nColuna 'FABRICANTE'")
print("Entropia: {:.4}".format(entropia_fabricante * -1))
print("Entropia Máxima: {:.4}".format(log(classes_fabricante, 2)))