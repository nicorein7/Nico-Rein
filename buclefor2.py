estudiante = {
  'nombre':'nicolas',
  'apellido':'rein'}
for clave , valor in estudiante.items():
  print(clave,':',valor)
for nombre , valor in estudiante.items():
  print(valor)

Numeros = [1, 6, 2.4, 5, 8, -4, 12, -5]
Contador = 0
for Lista in Numeros:
  if Lista < 0:
    Contador +=1
print(f'El total de números negativos es:'{Contador})


Dorsales = [3, 5, 19, 4, 7]
for Lista2 in Dorsales:
  if Lista2 > 10:
    print('El primer dorsal mayor que 10 es:', Lista2)
  