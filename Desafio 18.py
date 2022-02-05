#Seno, Cosseno e Tangente (Precisa converter o angulo em radiano!)

import math
ang = float(input('Informe um Ângulo: '))
seno = math.sin(math.radians(ang))
print('O Seno do Ângulo {}° é {:.4f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O Cosseno do Ângulo {}° é {:.4f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O Tangente do Ângulo {}° é {:.4f}'.format(ang, tan))
