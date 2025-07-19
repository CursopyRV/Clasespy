
from modulos.sistema import Sistema

sistema = Sistema ()

while True:
    sistema.mostrar_menu()

    opcion = input("Seleccione una opcion (1-4):")

    if opcion == "1":
        sistema.ver_transacciones()
    elif opcion == "2":
        sistema.agregar_transacciones()
    elif opcion == "3":
        sistema.validar_transacciones()
    elif opcion == "4":
        print("Saliendo del sistema. Gracias por utilizar nuestro servicio!")
        break
    else:
        print("Opción no valida. Intente nuevamente")
        


