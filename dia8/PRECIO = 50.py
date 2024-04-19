PRECIO = 50

class PYTimesUser:
    def _init_(self, nombre, precio_suscripcion=PRECIO):
        self.nombre = nombre
        self.precio_suscripcion = precio_suscripcion
        self.suscripciones = []
        self.valor = 0

    def agregar(self, año):
        self.suscripciones.append(año)

    def suscribir(self, año):
        if self.valor >= self.precio_suscripcion:
            self.valor -= self.precio_suscripcion
            self.agregar(año)
            print(f"Suscripción al año {año} realizada con éxito por {self.nombre}")
        else:
            print(f"No hay suficiente dinero ({self.valor}) para comprar suscripción")

    def depositar(self, cantidad):
        self.valor += cantidad

    def comprar(self, otro_usuario, año):
        if self.valor >= otro_usuario.precio_suscripcion:
            self.valor -= otro_usuario.precio_suscripcion
            otro_usuario.agregar(año)
            print(f"({self.nombre}) Compró la suscripción de regalo de {otro_usuario.nombre} para el año {año}")
        else:
            print(f"No hay suficiente dinero ({self.valor})")

    def obtener_suscripcion(self):
        return self.precio_suscripcion

    def obtener_nombre(self):
        return self.nombre

nombre = input("Ingresa tu nombre: ")
cel = PYTimesUser(nombre)
cantidad = int(input("Ingrese su cantidad de dinero: "))
cel.depositar(cantidad)

año = int(input("Año de suscripción: "))
cel.suscribir(año)

nombre_otro = input("Ingresa nombre a quien harás el regalo: ")
otro_usuario = PYTimesUser(nombre_otro)
regalo = int(input("Año de suscripción para el regalo: "))
cel.comprar(otro_usuario, regalo)

print(f"La suscripción de {cel.obtener_nombre()}: {cel.suscripciones}")