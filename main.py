from modelos.servicio import ServicioSala, ServicioEquipo, ServicioAsesoria

s1 = ServicioSala("Sala básica", 50)
s2 = ServicioEquipo("Computador", 30)
s3 = ServicioAsesoria("Consultoría", 100)

print(s1.calcular_costo(2))
print(s2.calcular_costo(2))
print(s3.calcular_costo(2))