import re

def hallar_numericos(s):
  ##verifica si existen las x e y 
  if 'x' in s and 'y' in s:
    ##Separa los numeros de un str
    s_numeric = [float(s) for s in re.findall(r'-?\d+\.?\d*', s)]
    #ORDENA LOS VALORES DE X E Y
    if s.find('x') > s.find('y'):
      s_numeric = list(reversed(s_numeric))
    return s_numeric
  else:
    print('Ingrese un string valido')
    return None, None
   
    


s = '10x+ 20y'
s2 = '20y+ 10x'
s3 = 'cualquierx cosa'

print(hallar_numericos(s))
print(hallar_numericos(s2))
print(hallar_numericos(s3))