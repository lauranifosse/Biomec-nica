xc1 = float(input('Digite o valor do Eixo 1 - Câmera A: '))
yc1 = float(input('Digite o valor do Eixo 2 - Câmera A: '))

xc2 = float(input('Digite o valor do Eixo 1 - Câmera B: '))
yc2 = float(input('Digite o valor do Eixo 2 - Câmera B: '))

xp1 = float(input('Digite o valor do Eixo 1 - Projeção A: '))
yp1 = float(input('Digite o valor do Eixo 2 - Projeção A: '))

xp2 = float(input('Digite o valor do Eixo 1 - Projeção B: '))
yp2 = float(input('Digite o valor do Eixo 2 - Projeção B: '))

mr1 = (yp1 - yc1)/(xp1 - xc1)
mr2 = (yp2 - yc2)/(xp2 - xc2)

br1 = -1*(mr1*xc1-yc1)
br2 = -1*(mr2*xc2-yc2)

x = (-(mr2*xc2) + yc2 + (mr1*xc1) - yc1) / (mr1-mr2)
y = (mr1 * x) - (mr1 * xc1) + yc1

print('Pontos de Intersecção: (', x, ',',y,')')

x1=[xc1, xp1]
y1=[yc1, yp1]
x2=[xc2, xp2]
y2=[yc2, yp2]

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot(x1,y1,x2,y2) 

plt.xlabel('Eixo 1')
plt.ylabel('Eixo 2')
        
plt.show()