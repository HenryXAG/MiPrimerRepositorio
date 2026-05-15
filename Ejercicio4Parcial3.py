def ejecutarAuditoria():
    print("-- SISTEMA DE AUDITORÍA DE REGISTROS --")
    print("Iniciando escaneo de los 50 sectores...\n")

    for numero in range(1, 51):

        if numero == 42:
            print("¡ALERTA CRÍTICA! Brecha de seguridad en registro ID:", numero)
            print("Abortando la auditoría inmediatamente...")
            break

        if numero % 3 == 0:
            continue
        print("Procesando registro ID:", numero)

    print("\n-- PROTOCOLO DE AUDITORÍA FINALIZADO --")


if __name__ == "__main__":
    ejecutarAuditoria()
