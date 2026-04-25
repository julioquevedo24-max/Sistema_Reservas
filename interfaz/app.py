import tkinter as tk
from tkinter import ttk, messagebox

from modelos.cliente import Cliente
from modelos.servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from modelos.reserva import Reserva
from excepciones.error_sistema import ErrorSistema


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas - Software FJ")
        self.root.geometry("600x500")

        # Listas en memoria
        self.clientes = []
        self.reservas = []

        # Servicios disponibles (polimorfismo)
        self.servicios = {
            "Sala": ServicioSala("Sala", 50),
            "Equipo": ServicioEquipo("Equipo", 30),
            "Asesoría": ServicioAsesoria("Asesoría", 100)
        }

        self.crear_interfaz()

    # =========================
    # INTERFAZ
    # =========================
    def crear_interfaz(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        # ---------- CLIENTE ----------
        ttk.Label(frame, text="Nombre").grid(row=0, column=0)
        self.nombre = ttk.Entry(frame)
        self.nombre.grid(row=0, column=1)

        ttk.Label(frame, text="Documento").grid(row=1, column=0)
        self.documento = ttk.Entry(frame)
        self.documento.grid(row=1, column=1)

        ttk.Label(frame, text="Correo").grid(row=2, column=0)
        self.correo = ttk.Entry(frame)
        self.correo.grid(row=2, column=1)

        ttk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente)\
            .grid(row=3, columnspan=2, pady=5)

        # ---------- RESERVA ----------
        ttk.Label(frame, text="Servicio").grid(row=4, column=0)
        self.combo_servicio = ttk.Combobox(frame, values=list(self.servicios.keys()))
        self.combo_servicio.grid(row=4, column=1)

        ttk.Label(frame, text="Horas").grid(row=5, column=0)
        self.horas = ttk.Entry(frame)
        self.horas.grid(row=5, column=1)

        ttk.Button(frame, text="Crear Reserva", command=self.crear_reserva)\
            .grid(row=6, columnspan=2, pady=5)

        ttk.Button(frame, text="Confirmar Última", command=self.confirmar_reserva)\
            .grid(row=7, column=0)

        ttk.Button(frame, text="Cancelar Última", command=self.cancelar_reserva)\
            .grid(row=7, column=1)

        # ---------- RESULTADOS ----------
        self.salida = tk.Text(frame, height=12, width=70)
        self.salida.grid(row=8, columnspan=2, pady=10)

    # =========================
    # FUNCIONES
    # =========================
    def registrar_cliente(self):
        try:
            cliente = Cliente(
                self.nombre.get(),
                self.documento.get(),
                self.correo.get()
            )
            self.clientes.append(cliente)
            messagebox.showinfo("Éxito", "Cliente registrado")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def crear_reserva(self):
        try:
            if not self.clientes:
                raise ErrorSistema("Debe registrar al menos un cliente")

            cliente = self.clientes[-1]
            servicio = self.servicios[self.combo_servicio.get()]
            horas = float(self.horas.get())

            reserva = Reserva(cliente, servicio, horas)
            self.reservas.append(reserva)

            self.salida.insert(tk.END, f"{reserva}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def confirmar_reserva(self):
        try:
            if not self.reservas:
                raise ErrorSistema("No hay reservas")

            self.reservas[-1].confirmar()
            self.salida.insert(tk.END, "Reserva confirmada\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cancelar_reserva(self):
        try:
            if not self.reservas:
                raise ErrorSistema("No hay reservas")

            self.reservas[-1].cancelar()
            self.salida.insert(tk.END, "Reserva cancelada\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()