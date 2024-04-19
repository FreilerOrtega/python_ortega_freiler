#carrito de compra 
carrito=[] #creamos el array vacio donde agregaremos los productos que vamos a comprar

cantidad=int(input("cuantos productos vas a comprar  : "))
for i in range(cantidad):                                     #creamos el bucle que se utilizara para llenar nuestro carrito
    nombre=str(input("nombre de el producto : "))             # cada una de las entradas se guardaran en la parte correspondiente de el arreglo
    precio=int(input("ingrese el valor de el producto : "))
    cantidad=int(input("ingrese la cantidad de productos : "))
    carrito.append([nombre,precio,cantidad ])
    


print(carrito) #mostramos la lista de los productos que se agregaron

