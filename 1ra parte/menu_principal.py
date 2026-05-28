estudiantes=[]
while True:
    print("\n1. registrar estudiante")
    print("2. ver estudiantes ")
    print('escribe salir para salir')
    break
#control de errores con strip y lower
opcion= input("opcion:")
opcion= opcion.strip()
opcion= opcion.lower()

if opcion == "1":
    nombre= input("nombre del estudiante: ")
    ruta= input("ruta que usa: ")

elif opcion == "2":
    if estudiantes == []: