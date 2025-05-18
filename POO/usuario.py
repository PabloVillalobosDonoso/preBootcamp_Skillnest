from tarjetas_credito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [TarjetaCredito(30000, 0.015)]

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        if self.tarjetas[0].limite_credito < (self.tarjetas[0].saldo_pagar + monto):
            print("¡COMPRA RECHAZADA! Exceso de limite de credito")
        else:
            self.tarjetas[0].saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self

    def pagar_tarjeta(self,monto):
        self.tarjetas[0].saldo_pagar -= monto
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar ${self.tarjetas[0].saldo_pagar}")
        return self
    
    def transferir_deuda(self, otro_usuario, monto):
        self.tarjetas[0].saldo_pagar -= monto
        otro_usuario.tarjetas[0].saldo_pagar += monto
        return self

    def agregar_tarjeta(self):
        self.tarjetas.append(TarjetaCredito(35000, 0.2, 0))
        for tarjeta in self.tarjetas:
            print(tarjeta.limite_credito, tarjeta.interes, tarjeta.limite_credito)