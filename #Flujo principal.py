#PROYECTO FINAL - GENERADOR DE RETRABAJOS
#Proceso: Ensamblaje de Control de Videojuego

#Flujo Principal
main_flow = [
    "Soldar Circuitos",
    "Ensamblar Carcasa",
    "Instalar Componentes",
    "Probar Controles",
    "Grabado Laser",
    "Empacar Producto"
]

#Datos de los retrabajos
reworks = {
    "Falla de Bluetooth": {
        "detected_in": "Probar Controles",
        "go_to_path": "Re-soldado Chip/Desmontar Placa",
        "return_step": "Soldar Circuitos",
        "reason": "Falla de Bluetooth"
    },
    "Carcasa Rayada": {
        "detected_in": "Empacar Producto",
        "go_to_path": "Reemplazo Estetico/Desarmar Plasticos",
        "return_step": "Ensamblar Carcasa",
        "reason": "Carcasa Rayada"
    }
}

def mostrar_flujo_principal():
    print("FLUJO PRINCIPAL: Ensamblaje de Control de Videojuego")
    print("="*70)
    for i, step in enumerate(main_flow, 1):
        print(f"{i}. {step}")
    print("\n")


def generar_retrabajo(reason):
    if reason in reworks:
        r = reworks[reason]
        
        print("\n")
        print(f"          OUTPUT GENERADO - Detectado en: {r['detected_in']}")
        
        output = (
            f"GoToFlowPath[{r['go_to_path']}]\n"
            f"ReturnStep[{r['return_step']}]\n"
            f"Reason[{r['reason;']}]"
        )
        
        print(output)
        print("\n")

        #Guardar en archivo
        with open("retrabajos_generados.txt", "a", encoding="utf-8") as f:
            f.write(f"\n=== Retrabajo: {reason} ===\n")
            f.write(f"Detectado en: {r['detected_in']}\n")
            f.write(output + "\n")
            f.write("="*50 + "\n")
        
        print("Guardado correctamente en 'retrabajos_generados.txt'\n")
    else:
        print("\nNo existe un retrabajo para esa razon.\n")


#Menu Principal
def main():
    print("GENERADOR DE RETRABAJOS - Iniciado\n")
    
    while True:
        print("-"*60)
        print("              MENU PRINCIPAL")
        print("-"*60)
        print("1. Ver Flujo Principal")
        print("2. Generar Retrabajo")
        print("3. Salir")
        print("-"*60)

        option = input("\nSelecciona una opcion (1-3): ").strip()

        if option == "1":
            mostrar_flujo_principal()
            
        elif option == "2":
            print("\nRazones disponibles:")
            for reason in reworks.keys():
                print(f"   - {reason}")
            print()
            
            user_reason = input("Ingresa la razon del fallo: ").strip()
            generar_retrabajo(user_reason)
            
        elif option == "3":
            print("\nSaliendo del programa... Exito con la entrega!")
            break
        else:
            print("\nOpcion invalida. Por favor intenta de nuevo.\n")


if __name__ == "__main__":
    main()