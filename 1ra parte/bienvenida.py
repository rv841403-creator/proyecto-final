estudiantes= {}
puntos_seguro={} 
dni=()
accion=()
id_punto=()
false=()
archivo=()
while True: 
 print("\n=== sistema ruta protegida ===")
 print("1. iniciar sesion  admin")
 print("2. registrar estudiante")
 print("3. salir del sistema")
 break 
opcion= input ("elige una opcion:")
if opcion=="1":
    usuario= input ("\nusuario admin :").strip()
    contraseña= input ("contraseña : ").strip ()
    if usuario== "admin" and contraseña== "1234":
        print("\n acceso concedido. bienvenido admin!")
        print ("\n¿que quieres hacer?")
        print("1. registrar punto seguro")
        print("2. ver puntos seguros")
        print("3. ver estudiantes por ruta")

        accion= input ("elige una opcion:").strip ()
        if accion == "1":
           print("\n--- registrar punto seguro---")
           id_punto= input("ID del punto (ej: p01):").strip()

           if id_punto == "":
              print("error:el ID no puede estar vacio.")
        elif id_punto in puntos_seguro:
           print("error: ese ID ya existe")
        else:
           nombre= input("nombre del negocio/vecino:").strip()
           direccion= input ("direccion:").strip()
           encargado= input ("nombre del encargado:").strip()

           puntos_seguro[id_punto]={
              "nombre": nombre,
              "direccion": direccion,
              "encargado": encargado
           } 
           print(f" punto seguro '{nombre}' registrado correctamente")
    elif accion == "2":
           print ("\n---puntos seguros registrados")
           if not puntos_seguro:
               print("no hay puntos seguros registrados.")
           else:
               for id_p, datos in puntos_seguro.items():
                   print(f"{id_p}:{datos['nombre']}-{datos['direccion']}| encargado:{datos['encargado']}")

    elif  accion == "3":
           print ("\n--- estudiantes por ruta---")
           if not estudiantes:
               print("no hay estudiantes registrados.")
           else:
               ruta_buscar= input("ingresa la ruta/calle a buscar:").strip().lower()
               encontrados= false 
               for dni, datos in estudiantes.items():
                   if ruta_buscar in datos ["ruta"].lower():
                       print(f"DNI:{dni}| {datos['nombre']}|grado:{datos['grado']}")
                       encontrados= True
                       if not encontrados:
                           print("no se encontyraron estudiantes en esa ruta.")
                       else:
                           print("opcion invalida")
    else:
        print("usuario o contraseña incorrectos.")
elif opcion == "2":
    print ("\n--- registrar estudiante---")
    dni= input("ingresa DNI del estudiante: ").strip()
    if dni in estudiantes :
     print("error: ese estudiante ya esta registrado.")
    elif dni =="" or not dni.isdigit():
        print("error:ingresa un DNI valido solo con numeros.")
    else:
        nombre= input ("nombre completo:").strip()
    if nombre == "":
        print("error: el nombre no puede estar vacio.")
    else:
        grado= input("grado y seccion(ej:5A):").strip()
        ruta= input ("calle/ruta principal que usa para ir al colegio: ").strip()

        estudiantes[dni]={
            "nombre":nombre,
            "grado":grado,
            "ruta":ruta
        }   
        print(f"estudiante{nombre}registrado en la ruta: {ruta}")
elif opcion == "3" :
      datos = {
    "estudiantes":estudiantes,
    "puntos_seguro":puntos_seguro}
with open(archivo, "w" ,encoding="utf-8")as f :
    print("datos guardados.saliendo del ssitema...")

