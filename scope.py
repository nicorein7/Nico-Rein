variable_global = 'Esto es una variable global'
def scope():
  variable_local = 'Esto es una variable local'
  variable_global = "Esto es un variable global modificada"
  print(variable_local)
  print(variable_global) #Se puede redefinir desde dentro de una función (local), pero solo afectará a la función
scope()
#Se puede redefinir desde dentro de una función (local)
print(variable_local) #Esto dará error porque la variable solo está asociada a la def scope