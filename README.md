🧩 Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto desarrollado en Python como parte del curso de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

📌 Descripción

Este sistema permite gestionar:

👤 Clientes
🛠️ Servicios (salas, equipos y asesorías)
📅 Reservas

Fue desarrollado bajo el paradigma de Programación Orientada a Objetos (POO), sin uso de bases de datos, utilizando estructuras en memoria y manejo de archivos para el registro de eventos.

🎯 Objetivo

Construir una aplicación modular, extensible y robusta que implemente:

Abstracción
Herencia
Polimorfismo
Encapsulación
Manejo avanzado de excepciones
🧠 Tecnologías utilizadas
Python 3
Tkinter (interfaz gráfica)
Manejo de archivos (logs)
📂 Estructura del proyecto
Sistema_Reservas/
│
├── main.py
├── modelos/
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva.py
│
├── excepciones/
│   └── error_sistema.py
│
├── interfaz/
│   └── app.py
│
├── logs/
│   └── sistema.log
│
└── README.md
⚙️ Funcionalidades principales

✔ Registro de clientes con validaciones
✔ Creación de servicios mediante herencia
✔ Gestión de reservas (confirmación y cancelación)
✔ Cálculo de costos con polimorfismo
✔ Aplicación de descuentos
✔ Interfaz gráfica funcional
✔ Manejo de errores sin detener el sistema
✔ Registro automático de errores en archivo

🧪 Simulación del sistema

El sistema ejecuta 10 operaciones, incluyendo:

✔ Creación de cliente válido
❌ Intento de cliente inválido
✔ Reserva correcta
❌ Reserva con datos inválidos
✔ Confirmación de reserva
❌ Cancelación inválida
✔ Cálculo de costos por tipo de servicio
✔ Aplicación de descuento válido
❌ Intento de descuento inválido

Esto demuestra la capacidad del sistema para continuar funcionando ante errores.

⚠️ Manejo de excepciones

Se implementa:

Excepción personalizada (ErrorSistema)
Bloques try / except
Validaciones estrictas
Registro de errores en archivo

Ejemplo de log:

2026-04-25 - ERROR - Cliente inválido: El nombre no puede estar vacío
📄 Registro de logs

Todos los errores se almacenan en:

logs/sistema.log

Esto permite auditar el comportamiento del sistema sin interrumpir su ejecución.

🖥️ Interfaz gráfica

El sistema cuenta con una interfaz desarrollada en Tkinter que permite:

Registrar clientes
Crear reservas
Confirmar o cancelar reservas
Visualizar resultados en pantalla
▶️ Ejecución del proyecto

Ubicarse en la carpeta raíz del proyecto y ejecutar:

python main.py

O para la interfaz gráfica:

python interfaz/app.py
📚 Principios de POO aplicados
Abstracción: clases abstractas (Entidad, Servicio)
Herencia: especialización de servicios
Polimorfismo: métodos calcular_costo()
Encapsulación: atributos privados y métodos de acceso
🏁 Conclusión

El sistema cumple con todos los requerimientos planteados en la actividad, demostrando el uso adecuado de la programación orientada a objetos y el manejo avanzado de excepciones en un entorno sin base de datos.

👨‍💻 Autor

Julio Quevedo
Estudiante de Ingeniería de Sistemas – UNAD