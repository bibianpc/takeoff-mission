import subprocess

# Ejecuta un comando bash
def fn_ejecutar_comando(comando):
  getList = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  salida, error =getList.communicate()
  return  salida, error