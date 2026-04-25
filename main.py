from modelos.cliente import Cliente

try:
    c1 = Cliente("Julio", "12345", "julio@email.com")
    print(c1)

    c2 = Cliente("", "abc", "correo_mal")  # error
except Exception as e:
    print(e)