from modelos.cliente import Cliente
from modelos.servicio import ServicioSala
from modelos.reserva import Reserva

try:
    cliente = Cliente("Julio", "12345", "julio@email.com")
    servicio = ServicioSala("Sala básica", 50)

    reserva = Reserva(cliente, servicio, 2)

    reserva.confirmar()

    print(reserva)
    print("Con descuento:", reserva.calcular_total_con_descuento(10))

except Exception as e:
    print(e)