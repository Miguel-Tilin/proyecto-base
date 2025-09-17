from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Resto (módulo)")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "6":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ["1", "2", "3", "4", "5"]:
            op.leerNumeros()
            if opcion == "1":
                op.sumar()
            elif opcion == "2":
                op.restar()
            elif opcion == "3":
                op.multiplicacion()
            elif opcion == "4":
                op.division()
            elif opcion == "5":
                op.resto()
            op.mostrarResultado()
        else:
            print("Opción inválida, intenta de nuevo.")

    
if __name__ == "__main__":
    main()
    
    