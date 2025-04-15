import os
import subprocess
import sys

def root():
    return os.geteuid() == 0

def actualizar():
    print("Actualizando lista de paquetes...")
    subprocess.run(["apt", "update"], check=True)
    
    print("\n Ejecutando la instalacion de paquetes...")
    subprocess.run(["apt", "full-upgrade", "-y"], check=True)

    print("\n Ejecutando autoremove para limpiar paquetes innecesarios...")
    subprocess.run(["apt", "autoremove", "-y"], check=True)

    print("\n !Sistema actualizado y limpiado correctamente¡")

if __name__ == "__main__":
    if not root():
        print("Este script debe ejecutarse como root (usa sudo).")
        sys.exit(1)

    try:
        actualizar()
    except subprocess.CalledProcessError as e:
        print(f" Ha ocurrido un error durante la actualización: {e}")
        sys.exit(1)
