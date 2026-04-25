from abc import ABC, abstractmethod
from excepciones.error_sistema import ErrorSistema

# =========================
# CLASE ABSTRACTA
# =========================
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        try:
            self.set_nombre(nombre)
            self.set_precio_base(precio_base)
        except Exception as e:
            raise ErrorSistema(f"Error al crear servicio: {e}")

    # =========================
    # GETTERS
    # =========================
    def get_nombre(self):
        return self.__nombre

    def get_precio_base(self):
        return self.__precio_base

    # =========================
    # SETTERS CON VALIDACIÓN
    # =========================
    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
        self.__nombre = nombre.strip()

    def set_precio_base(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        self.__precio_base = precio

    # =========================
    # MÉTODO ABSTRACTO (POLIMORFISMO)
    # =========================
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# SERVICIO SALA
# =========================
class ServicioSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorSistema("Horas inválidas para sala")
        return self.get_precio_base() * horas

    def descripcion(self):
        return f"Servicio de Sala - ${self.get_precio_base()}/hora"


# =========================
# SERVICIO EQUIPO
# =========================
class ServicioEquipo(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorSistema("Horas inválidas para equipo")
        costo = self.get_precio_base() * horas
        return costo + 20  # recargo fijo

    def descripcion(self):
        return f"Alquiler de Equipos - ${self.get_precio_base()}/hora + recargo"


# =========================
# SERVICIO ASESORÍA
# =========================
class ServicioAsesoria(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorSistema("Horas inválidas para asesoría")
        return (self.get_precio_base() * horas) * 1.15  # incremento 15%

    def descripcion(self):
        return f"Asesoría Especializada - ${self.get_precio_base()}/hora + 15%"