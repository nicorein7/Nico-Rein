def saludos():
  print('Bienvenido')
saludos()

def buy(list,budget):
  print(f"Mi lista de la compra es: {list} y tengo {budget} €")
buy(['patatas', 'aceite', 'cebolla'], 33)
buy(['camiseta', 'calcetines', 'zapatillas'], 123)

def carrito(list_prices):
  total=0
  for precio in list_prices:
     total += precio
  return total
carrito_user1 = carrito([4,6,7,8,3,12])
print (f"El total de la compra es {carrito_user1} €")
carrito_user2 = carrito([3,8,3,11,15,9])
print(f"El total de la compra 2 es {carrito_user2} €")

def valoracion_restaurante(puntuaciones):
  valoracion_máxima = puntuaciones[0]
  for puntuación in puntuaciones:
    if puntuación > valoracion_máxima:
      valoracion_máxima = puntuación
  return valoracion_máxima
restaurantes_madrid = valoracion_restaurante([3,4,5,4,2,4,3])
restaurantes_bcn = valoracion_restaurante([3.2,4.5,4.9,2.3,3.3])
print (f"La mayor valoración de restaurante en Madrid es {restaurantes_madrid} puntos")
print (f"La mayor valoracion de restaurante en Barcelona es {restaurantes_bcn} puntos")