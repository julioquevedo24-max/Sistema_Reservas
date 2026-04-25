from modelos.cliente import Cliente
from modelos.servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from modelos.reserva import Reserva
from excepciones.error_sistema import ErrorSistema
import logging
import os

# Crear carpeta logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def simular_operaciones():
    operaciones = []

    # Servicios
    sala = ServicioSala("Sala", 50)
    equipo = ServicioEquipo("Equipo", 30)
    asesoria = ServicioAsesoria("Asesoría", 100)

    # 1. Cliente válido
    try:
        c1 = Cliente("Juan", "12345", "juan@email.com")
        operaciones.append("Cliente válido creado")
    except Exception as e:
        logging.error(e)

    # 2. Cliente inválido
    try:
        c2 = Cliente("", "abc", "correo")
    except Exception as e:
        logging.error(f"Cliente inválido: {e}")
        operaciones.append("Error en cliente inválido")

    # 3. Reserva válida
    try:
        r1 = Reserva(c1, sala, 2)
        operaciones.append("Reserva válida creada")
    except Exception as e:
        logging.error(e)

    # 4. Reserva con horas inválidas
    try:
        r2 = Reserva(c1, sala, -1)
    except Exception as e:
        logging.error(f"Reserva inválida: {e}")
        operaciones.append("Error en reserva inválida")

    # 5. Confirmar reserva
    try:
        r1.confirmar()
        operaciones.append("Reserva confirmada")
    except Exception as e:
        logging.error(e)

    # 6. Cancelar reserva confirmada (error)
    try:
        r1.cancelar()
    except Exception as e:
        logging.error(f"Cancelación inválida: {e}")
        operaciones.append("Error al cancelar confirmada")

    # 7. Servicio equipo
    try:
        r3 = Reserva(c1, equipo, 3)
        operaciones.append(f"Reserva equipo: {r3.calcular_total()}")
    except Exception as e:
        logging.error(e)

    # 8. Servicio asesoría
    try:
        r4 = Reserva(c1, asesoria, 2)
        operaciones.append(f"Reserva asesoría: {r4.calcular_total()}")
    except Exception as e:
        logging.error(e)

    # 9. Descuento válido
    try:
        total_desc = r3.calcular_total_con_descuento(10)
        operaciones.append(f"Total con descuento: {total_desc}")
    except Exception as e:
        logging.error(e)

    # 10. Descuento inválido
    try:
        r3.calcular_total_con_descuento(200)
    except Exception as e:
        logging.error(f"Descuento inválido: {e}")
        operaciones.append("Error en descuento")

    return operaciones


if __name__ == "__main__":
    resultados = simular_operaciones()

    print("=== SIMULACIÓN ===")
    for r in resultados:
        print(r)