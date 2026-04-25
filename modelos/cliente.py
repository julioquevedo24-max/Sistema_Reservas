from abc import ABC, abstractmethod
from excepciones.error_sistema import ErrorSistema

# =========================
# CLASE ABSTRACTA
# =========================
class Entidad(ABC):
    @abstractmethod
    def mostrar(self):
        pass


# =========================
# CLASE CLIENTE
# =========================
class Cliente(Entidad):
    def __init__(self, nombre, documento, correo):
        try:
            self.set_nombre(nombre)
            self.set_documento(documento)
            self.set_correo(correo)
        except Exception as e:
            raise ErrorSistema(f"Error al crear cliente: {e}")

    # =========================
    # GETTERS
    # =========================
    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    # =========================
    # SETTERS CON VALIDACIÓN
    # =========================
    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre.strip()

    def set_documento(self, documento):
        if not documento.isdigit():
            raise ValueError("El documento debe ser numérico")
        self.__documento = documento

    def set_correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido")
        self.__correo = correo

    # =========================
    # MÉTODO ABSTRACTO IMPLEMENTADO
    # =========================
    def mostrar(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento} | Correo: {self.__correo}"

    # =========================
    # MÉTODO EXTRA
    # =========================
    def __str__(self):
        return self.mostrar()