from modulos.transacciones import transaccion


class Sistema:

    def __init__(self):
        self.transacciones = []

    def mostrar_menu(self):
        print(f"\n---MENU DE OPERACIONES---")
        print("1. Ver transacciones")
        print("2. Agregar una nueva transaccion")
        print("3. Validar transacciones")
        print("4. Salir")

    def ver_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas")
        else:
            print("Lista de transacciones:")
            for t in self.transacciones:
                print(t)

    def agregar_transacciones(self):
        try:
            monto = float(input("Ingrese el monto de la transacción: "))
            moneda = input("Ingrese la moneda (ARS/USD):").upper()
            if moneda not in ("ARS", "USD"):
                print("Moneda ingresada incorrecta")
                return
            nueva_transaccion = transaccion(id= len(self.transacciones)+ 1, monto=monto, moneda=moneda)
            self.transacciones.append(nueva_transaccion)
            print("Transaccion agregada correctamente")
        except ValueError:
            print("Error: El monto debe ser un número")

    def validar_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas")
        else:
            print("Validación de transacciones: ")
            for t in self.transacciones:
                estado = t.validar()
                print(f"{t} ->{estado}")