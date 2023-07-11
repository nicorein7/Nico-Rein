y = 1
while y <= 3:
  print (y)
  y +=1

tareas = ['Limpiar', 'Planchar', 'Comprar', 'Recoger']
while len(tareas) > 0:
  check = tareas.pop(0)
  print(f'Quedan {len(tareas)+1} tareas')
  print(f'{check} Completado')
print("Tareas terminadas")