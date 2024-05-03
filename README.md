# Desafio Guiado - Vehiculos Empresa

# Fleet Management System

## Descripción

El propósito de este desafío es modelar un sistema básico que permita la gestión de flotas de vehículos utilitarios, incluyendo su asignación a conductores y su registro en la contabilidad.

## Objetivos

- Implementar un Proyecto Django: Crear un proyecto denominado "fleetmanager" y dentro de él, una aplicación llamada "fleetApp".

- Modelado de Datos: Configurar tres modelos principales: `Driver`, `Vehicle` y `AccountingRecord`. 
    - `Driver` tendrá los campos `rut`, `name`, `last_name`, `active`, `created_at` y una relación uno a uno con `Vehicle`.
    - `Vehicle` tendrá los campos `registration_plate`, `brand`, `model`, `year`, `active` y `created_at`.
    - `AccountingRecord` tendrá los campos `purchase_date`, `price` y una relación uno a uno con `Vehicle`.

- Configuración de Base de Datos: Usar PostgreSQL para almacenar los datos.

- Servicios de Aplicación:
    - Crear servicios que permitan:
    - Crear vehículos, conductores y registros contables.
    - Deshabilitar y habilitar vehículos y conductores.
    - Asignar conductores a vehículos.
    - Obtener información detallada de los vehículos.
    - Imprimir información de los vehículos.

## Empezando 🚀

Para realizar este desafio, necesitas tener Python 3 instalado en tu sistema. Se recomienda usar un navegador web moderno como Google Chrome para acceder a la documentación en inglés y permitir la traducción automática del contenido.

### Pre-requisitos 📋

- Python 3.
- PostgreSQL.
- Conocimientos básicos de programación en Python.
- Conocimientos básicos de uso de la terminal o consola de comandos.
- Acceso a Internet para consultar la documentación oficial de Django y tutoriales complementarios.
- Librerias indicadas en el archivo "requeriments.txt"

## Autores ✒️

- **Emilio Madrid** - [EmilioMadridA](https://github.com/EmilioMadridA)

## Agradecimientos 🎁

- A todo el equipo de Desafio Latam y Talento Digital por la oportunidad de aprender y crecer en el campo del desarrollo web con Python y Django.
- A Brayan y Gustavo, por todo lo enseñado.