# %% Importar rnadom
import random


# %% Definir una funcion de revisar cada casilla alrededor del grid a fuerza bruta.
def revisar(a, b):
    c = 0
    for i in range(len(grid)):
        y = a
        y = y + 1 - i
        if y >= 0:
            for j in range(len(grid)):
                x = b
                x = x + 1 - j
                if x >= 0:
                    try:
                        c += grid[x][y]
                    except:
                        continue
    return c


# %% Resto de codigo lol
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in grid:
    print(i)

mx, my = random.randint(0, 2), random.randint(0, 2)

grid[mx][my] = 1

for i in grid:
    print(i)

hay = revisar(0, 0)

print(hay)
