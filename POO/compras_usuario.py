from usuario import Usuario
from tarjetas_credito import TarjetaCredito

pablo = Usuario("Pablo", "Villalobos", "pablo.villalobosdonoso@gmail.com")
vero = Usuario("Veronica", "Guajardo", "vero.gc@gmail.com")
pedro = Usuario("Pedro", "Henriquez", "pedro.h@gmail.com")



pablo.hacer_compra(500).hacer_compra(700).pagar_tarjeta(200).mostrar_saldo_usuario()
vero.hacer_compra(1300).pagar_tarjeta(150).pagar_tarjeta(600)
pablo.transferir_deuda(vero, 300).mostrar_saldo_usuario()
vero.mostrar_saldo_usuario()

pedro.hacer_compra(2344).hacer_compra(23423).hacer_compra(2322).pagar_tarjeta(5675).pagar_tarjeta(5675).pagar_tarjeta(5456).pagar_tarjeta(4579).mostrar_saldo_usuario()

tarjeta_pablo = TarjetaCredito(30000, 0.015)
tarjeta_vero = TarjetaCredito(55000, 0.01, 1000)

print(tarjeta_pablo.limite_credito, tarjeta_pablo.interes, tarjeta_pablo.saldo_pagar)
print(tarjeta_vero.limite_credito, tarjeta_vero.interes, tarjeta_vero.saldo_pagar)

tarjeta_pablo.compra(4500)
tarjeta_vero.compra(10000)

tarjeta_pablo.pago(1300)
tarjeta_vero.pago(5000)

tarjeta_pablo.mostrar_info_tarjeta()
tarjeta_vero.mostrar_info_tarjeta()

tarjeta_pablo.cobrar_interes()
tarjeta_vero.cobrar_interes()

tarjeta_pablo.mostrar_info_tarjeta()
tarjeta_vero.mostrar_info_tarjeta()

print("-----------------PRACTICA------------------")

tarjeta_nueva = TarjetaCredito(25000, 0.02, 4000)

tarjeta_pablo.compra(200).compra(300).pago(1500).cobrar_interes().mostrar_info_tarjeta()
tarjeta_vero.compra(600).compra(700).compra(150).pago(700).pago(2000).cobrar_interes().mostrar_info_tarjeta()
tarjeta_nueva.compra(5000).compra(7000).compra(4500).compra(10000).compra(15000).mostrar_info_tarjeta()

TarjetaCredito.mostrar_info_todas_tarjetas()

print("-----------------PRACTICA 2------------------")

pablo.tarjetas[0].mostrar_info_tarjeta()

pablo.tarjetas[0].compra(2000).compra(300).pago(1500).cobrar_interes().mostrar_info_tarjeta()
vero.tarjetas[0].compra(6000).compra(700).compra(150).pago(700).pago(2000).cobrar_interes().mostrar_info_tarjeta()
pedro.tarjetas[0].compra(5000).compra(7000).compra(4500).compra(10000).compra(15000).mostrar_info_tarjeta()

pablo.agregar_tarjeta()