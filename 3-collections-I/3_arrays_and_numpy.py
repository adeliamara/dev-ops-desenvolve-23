import array as arr


array = arr.array('d', [1,3.5])

print(array)
#os arrays sao de um mesmo tipo, o d identificar o double
#no python, praticamente nao usamos arrays

#preferimos usar o numpy se precisamos de trabalho numerico em detrimento ao array

import numpy as np

numeros = np.array([1.,3.5])

print(numeros + 3)