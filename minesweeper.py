# %% Importar rnadom
import random


# %% Definir una funcion de revisar cada casilla alrededor del grid a fuerza bruta.
def revisar(x, y):
    b = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            try:
                b += grid[x + 1 - i][y + 1 - j]
            except:
                continue
    return b


# %% Resto de codigo lol
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in grid:
    print(i)

mx, my = random.randint(0, 2), random.randint(0, 2)

grid[mx][my] = 1

for i in grid:
    print(i)

hay = revisar(2, 2)

print(hay)
