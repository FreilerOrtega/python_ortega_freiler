cant =int(input("ingresa la cantidad a cambiar :")) #pedimos al usuario que ingrese la cantidad que quiere cambiar 

monedas=[10,5,1]

def cambio_m(cantidad,monedas,resultado): #creamos la funcion para resolver el problema planteado
    if cantidad > 0 and len(monedas) > 0:
        monedamax = max(monedas)
        if cantidad - monedamax >= 0:
            valor = resultado.get("monedas de " + str(monedamax))
            if valor is None:
                resultado.update({"monedas de " + str(monedamax) : 1 })
            else:
                resultado.update({"monedas de " + str(monedamax): valor + 1})  
            cantidad=cantidad - monedamax 
        else:
            monedas.remove(monedamax)
        return cambio_m (cantidad,monedas,resultado)
    else:
        return resultado


print(cambio_m(cant,monedas,{})) #mostramos la repues con el valor de cada moneda y el numero de monedas usadas

# hecho por freiler aleiro ortega cc:1010075774