from src.utilities.utils import fn_ejecutar_comando
from src.business.analizador import Analizador

print("     #####################################################################")
print("     #####################################################################")
print("     #####                                                            ####")
print("     #####      #####    ###       ###        #####       ###         ####")
print("     #####      ######   ###      #####      ##          #####        ####")
print("     #####      #######  ###     ### ###      ###       ### ###       ####")
print("     #####      ### #### ###    ###   ###      ###     ###   ###      ####")
print("     #####      ###  #######   ###     ###       ##   ###     ###     ####")
print("     #####      ###   ######  ###       ###  #####   ###       ###    ####")
print("     #####                                                            ####")
print("     #####____________________________________________________________####")
print("     #####                                                            ####")
print("     #####                Sistema de Monitoreo Unificado              ####")
print("     #####                                                            ####")
print("     #####                         A P O L L O  11                    ####")
print("     #####                                                            ####")
print("     #####                 Integrantes: Bibiana Caicedo               ####")
print("     #####                                                            ####")
print("     #####################################################################")
print("     #####################################################################")
print(" ")

ejecutar = True
while ejecutar == True:
    print("\n--- OPCIONES ----")
    print("1. Generar informacion de dispositivos")
    print("2. Generar Estadisticas")
    print("3. SALIR")
    respuesta = input("\nSeleccione la opcion: ")
    mi_analizador = Analizador()

    if respuesta == "1":
        datos, error = fn_ejecutar_comando("apollo-11.sh")
        resultado =str(datos).split("\\n")
        print("RESULT==>", resultado[:-1])
        print("ERROR==>", error)

    elif respuesta == "2": 
        # Agrupa por dispositivos en una lista de diccionarios       
        valor = mi_analizador.fn_agrupar_por_dispositivos("D:\\\\AWS\\Phyton\\Trabajo_Final\\home\\bcaicedo\\takeoff-mission\\devices")
        # Genera el archivo de estadisticas y borra los logs
        mi_analizador.fn_crear_estadisticas(valor)

    elif respuesta == "3":  
        print("Ejecucion terminada")
        ejecutar = False
    else:
        print("\nOpcion incorrecta") 