print("===detector de contraseñas debiles ===")
print("escribe 'salir' para terminar/n")
while True:
    contraseña= input("escribe la contraseña: ").strip()
    #salir del programa
if contraseña.lowewr()== "salir": 
    print("saliendo...")
    'break' 
puntuaje=0
contraseña.lower=contraseña.lower()
#revisa todo
if len (contraseña)>=12:puntaje +=30
elif len (contraseña)>=8:puntaje +=15

if any(c.isupper()for c in contraseña): puntaje +=20
if any(c.islower()for c in contraseña): puntaje +=20
if any(c.isdigit()for c in contraseña): puntaje +=20
if any(c in "¡@#~~$%^*"()for c in contraseña): puntaje +=10
if not any ( p in contraseña_lower for p in ["123","abc","contraseña"] ): puntaje +=10

print("/npuntaje:",puntaje,"/100")
if puntaje >= 80: print ("nivel:FUERTE")
elif puntaje >= 50: print ("nivel:MEDIO")
else:print("nivel:DEBIL")
print("-------------------------/n")



