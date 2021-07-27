from pathlib import Path
from datetime import date
from os import remove

class Analizador:

    def __init__(self):
        pass

    # Lee el estado de un archivo especifico
    def fn_agrupar_por_dispositivos(self, ruta):
        # Lee los archivos .log que estan en la ruta
        files = Path(ruta).rglob("*.log")

        archivos_agrupados = {}

     
        for file in files:
            archivo = open(file)
            estado = archivo.readline()
            propietario = file.__getattribute__("owner")
            nombre = file.__getattribute__("name")
            peso = file.stat().st_size
            # ruta del archivo desde la raiz
            rutaarchivo = file.as_uri()
            indiceInicial = rutaarchivo.index("devices/") + len("devices/")
            fecha_carpeta = rutaarchivo[indiceInicial: indiceInicial + 10]
            if nombre.__contains__("ORB"):
                propietario = "orbit"
            elif nombre.__contains__("CNL"):
                propietario = "colony"
            elif nombre.__contains__("MRS"):
                propietario = "mars"
            else:
                propietario = "unknown"
            
            archivos_temp = archivos_agrupados.get(propietario, [] )
            archivos_temp.append({"nombre": nombre, "estado":estado, "peso": peso, "fecha": fecha_carpeta})
            archivos_agrupados[propietario] = archivos_temp
       
        return archivos_agrupados


    # Crear archivo de estadisticas
    def fn_crear_estadisticas(self, datos):
        current_date = date.today().strftime("%d%m%Y")
        # Crea el nombre del archivo incluyendo la ruta en el que se escriben las estadisticas
        nombre_archivo = "stats/APLSTATS-" + current_date + ".log"    
        archivo = open(nombre_archivo, "w")
        archivo.write("Nombre Archivo \t\tFecha \t\t\tPeso \t\tEstado\n")
        claves = datos.keys()
        
        for clave in claves:        
            elem_temp = datos.get(clave)        
            for elem in elem_temp:
                try:
                    archivo.write(elem.get("nombre") + "\t\t" + elem.get("fecha")  + "\t\t" + str(elem.get("peso")) + " Bytes\t\t" + elem.get("estado"))
                except Exception as ex:
                    print(f"No se encontro informacion para el dispositivo {clave}:{ex.args}")
                    break
        archivo.close()

        files = Path("D:\\\\AWS\\Phyton\\Trabajo_Final\\home\\bcaicedo\\takeoff-mission\\devices").rglob("*.log")

        for file in files:
            try:
                remove(file)
            except OSError as ex:
                print(f"Error al tratar de eliminar archivos:{ex.strerror}")