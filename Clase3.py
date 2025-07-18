
#for a in range(11):
#    print(a)

transacciones = []

while True:
    print("\n---MENU DE OPERACIONES---")
    print("1. Ver transacciones")
    print("2. Agregar una nueva transaccion")
    print("3. Validar transacciones")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4):")

    if opcion == "1":
        if not transacciones:
            print("No hay transacciones")
        else:
            print("lista de transacciones:")
            for t in transacciones:
                print("ID", t["id"], "|MONTO:", t["monto"], "|Moneda:", t["moneda"])
    elif opcion == "2":
        try:
            monto =  float(input("Ingrese el monto de la transacción: "))
            moneda = input("Ingrese la moneda (ARS/USD): ").upper()
            if moneda != "ARS" and moneda != "USD":
                print("Moneda ingresada incorrecta")
            else:
                nueva={
                    "id" : len(transacciones) + 1,
                    "monto" : monto,
                    "moneda": moneda
                }
                transacciones.append(nueva)
                print("transacción fue agregada con éxito!")
        except ValueError:
            print("Error: el monto debe ser un número")
    elif opcion == "3":
        if not transacciones:
            print("No hay transacciones registradas")
        else:
            print("Validación de transacciones: ")
            for t in transacciones:
                if t["monto"] <= 0:
                    estado= "Monto inválido"
                elif t["moneda"] == "ARS" and t["monto"] > 10000:
                    estado = "Requiere una autorización adicional"
                elif t["moneda"] == "USD" and t["monto"] > 10000:
                    estado = "Requiere una autorización adicional por monto en divisa USD"
                else:
                    estado = "Transacción validada!"
                print(f"ID: {t["id"]}, : {estado}")
    elif opcion == "4":
        print("Saliendo del sistema. Gracias por utilizar nuestro servicio!")
        break
    else:
        print("Opción no valida. Intente nuevamente")

                    
