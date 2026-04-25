from excepciones.error_sistema import ErrorSistema

# =========================
# CLASE RESERVA
# =========================
class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            self.set_cliente(cliente)
            self.set_servicio(servicio)
            self.set_horas(horas)
            self.__estado = "Pendiente"
        except Exception as e:
            raise ErrorSistema(f"Error al crear reserva: {e}")

    # =========================
    # SETTERS CON VALIDACIÓN
    # =========================
    def set_cliente(self, cliente):
        if cliente is None:
            raise ValueError("El cliente no puede ser nulo")
        self.__cliente = cliente

    def set_servicio(self, servicio):
        if servicio is None:
            raise ValueError("El servicio no puede ser nulo")
        self.__servicio = servicio

    def set_horas(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ValueError("Las horas deben ser un número mayor a 0")
        self.__horas = horas

    # =========================
    # GETTERS
    # =========================
    def get_cliente(self):
        return self.__cliente

    def get_servicio(self):
        return self.__servicio

    def get_horas(self):
        return self.__horas

    def get_estado(self):
        return self.__estado

    # =========================
    # MÉTODOS DE NEGOCIO
    # =========================
    def calcular_total(self):
        try:
            return self.__servicio.calcular_costo(self.__horas)
        except Exception as e:
            raise ErrorSistema(f"Error al calcular total: {e}")

    # =========================
    # SOBRECARGA SIMULADA (parámetro opcional)
    # =========================
    def calcular_total_con_descuento(self, descuento=0):
        try:
            total = self.calcular_total()
            if descuento < 0 or descuento > 100:
                raise ValueError("Descuento inválido")
            return total - (total * (descuento / 100))
        except Exception as e:
            raise ErrorSistema(f"Error en cálculo con descuento: {e}")

    # =========================
    # CAMBIO DE ESTADO
    # =========================
    def confirmar(self):
        if self.__estado == "Cancelada":
            raise ErrorSistema("No se puede confirmar una reserva cancelada")
        self.__estado = "Confirmada"

    def cancelar(self):
        if self.__estado == "Confirmada":
            raise ErrorSistema("No se puede cancelar una reserva ya confirmada")
        self.__estado = "Cancelada"

    # =========================
    # REPRESENTACIÓN
    # =========================
    def mostrar(self):
        try:
            return (
                f"Cliente: {self.__cliente.get_nombre()} | "
                f"Servicio: {self.__servicio.get_nombre()} | "
                f"Horas: {self.__horas} | "
                f"Estado: {self.__estado} | "
                f"Total: ${self.calcular_total():.2f}"
            )
        except Exception as e:
            raise ErrorSistema(f"Error al mostrar reserva: {e}")

    def __str__(self):
        return self.mostrar()