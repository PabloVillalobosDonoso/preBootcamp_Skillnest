class TarjetaCredito:
    #Atributos de clase
    banco = "Banco Internacional de Programadores"
    #Agregamos un atributo de clase que guarda todas las tarjetas de crédito
    todas_las_tarjetas = []
    def __init__(self, limite_credito, interes, saldo_pagar = 0):
        #Esteblecemos los atributos de instancia
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        self.interes = interes
        #Cada que se cree una nueva instancia de la clase, se agrega a todas_las_tarjetas
        TarjetaCredito.todas_las_tarjetas.append(self)

    #Método de clase que cambia el banco
    @classmethod
    def cambiar_banco(cls, nombre):
        cls.banco = nombre

    #Método de clase que imprime el total de saldos a pagar de todas las tarjetas
    def todos_saldos(cls):
        total_saldos = 0
        for tarjeta in cls.todas_las_tarjetas: #Usamos cls para hacer referencia a la clase
            total_saldos += tarjeta.saldo_pagar
        return total_saldos
    
    def compra(self, monto):
        if TarjetaCredito.validar_compra(self.limite_credito, self.saldo_pagar, monto):
            print("!COMPRA ACEPTADA!")
            self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        else:
            print("¡COMPRA RECHAZADA! Exceso de limite de credito")
        return self

    def pago(self, monto):
        #print(f"Saldo a pagar anterior: {self.saldo_pagar}")
        self.saldo_pagar -= monto
        #print(f"Nuevo saldo a pagar: {self.saldo_pagar}")
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar*self.interes
        return self

    @staticmethod
    def validar_compra(limite, saldo_pagar, monto):
        if (saldo_pagar + monto) > limite:
            return False
        return True
    
    @classmethod
    def mostrar_info_todas_tarjetas(cls):
        for tarjeta in cls.todas_las_tarjetas:
            print(tarjeta.saldo_pagar)