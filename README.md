# 🔄 Actualizador de Sistema Linux

Este script en Python automatiza el proceso de actualización de paquetes en sistemas basados en Debian (como Ubuntu), asegurando que el sistema esté completamente actualizado y limpio de paquetes innecesarios.

## 🚀 Funcionalidades

- Ejecuta `apt update` para actualizar la lista de paquetes.
- Ejecuta `apt full-upgrade -y` para instalar las últimas versiones disponibles.
- Ejecuta `apt autoremove -y` para eliminar paquetes no necesarios.
- Verifica que el script se ejecute con privilegios de superusuario (`root`).

## 📋 Requisitos

- Python 3.x
- Sistema basado en Debian/Ubuntu
- Privilegios de superusuario (`sudo`)

## 🛠️ Instalación

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/LordAguaKate/Actualizar_sistema_Linux_SCRIPT.git
```
