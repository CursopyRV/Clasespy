# Función para mostrar menú

def mostrar_menu():
    """Retorna con un print las opciones disponibles"""
    print(f"\n---MENU DE OPERACIONES---")
    print("1. Ver transacciones")
    print("2. Agregar una nueva transaccion")
    print("3. Validar transacciones")
    print("4. Salir")

#Función par ver transacciones(1)

def ver_transacciones(transacciones):
    """Retorna las listas de transacciones formateada"""
    if not transacciones:
        print("No hay transacciones")
    else:
        print("lista de transacciones:")
        for t in transacciones:
            print("ID", t["id"], "|MONTO:", t["monto"], "|Moneda:", t["moneda"])

# Función para agregar una nueva transaccion
def agregar_transaccion(transacciones):
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

#Funcion para validar las transacciones

def validar_transacciones(transacciones):
     
    if not transacciones :
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
     
