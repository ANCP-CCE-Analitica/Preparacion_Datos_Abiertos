# Preparación de datos abiertos

Trabajo conjunto con la subdirección de IDT para la preparación de datos abiertos.

## Estado actual del proyecto

En desarrollo

## Metodología utilizada

TDSP - Ampliar

- Exploración
- Análisis de estandarización
- Creación e implementación de funciones
- Pruebas y ajustes
- Documentación y publicación
- Revisión
- Paso a producción

## Estructura del proyecto

El proyecto se organiza en las siguientes carpetas y subcarpetas:

```
codigo (Contiene todo el código del proyecto)
|_ adquisicion y entendimiento de datos
|___ cuadernillos
|_____ libreria 
|_______ archivos.py (archivos usados en los cuadernillos)
|_____ archivos.ipynb
|___ reportes
|___ scripts (archivos que no son usados directamente por los cuadernillos (.sql, .py, etc))

documentos (Alojará todos los documentos del proyecto)
|_ analisis y descubrimientos
|_ diccionarios de datos
|_ gestion del proyecto

muestras de datos (Datos usados para validar, ejecutar o complementar los análisis que se requieran para el proyecto)
|_ auxiliar (archivos que complementan a la base principal del proyecto)
|_ procesados (datos que se procesaron con algúno de los cuadernillos del proyecto)
|_ sin procesar (datos en su versión pura o recien descargada de alguna de las fuentes de la agencia)

.gitignore (archivo en donde se alojarán todas las rutas de las bases que ya se encuentren en el datalake y los archivos de configuración que contengan credenciales de acceso)
```

## Requisitos de instalación y uso

Para poder utilizar SQL en Python es necesario instalar lo siguiente, escoja el driver de acuerdo al sistema operativo de su equipo: 
 
 
**Driver Microsoft ODBC para SQL SERVER en windows**
 
Descargar e instalar el driver de la página [Microsoft ODBC](https://docs.microsoft.com/en-us/sql/connect/odbc/windows/system-requirements-installation-and-driver-files?view=sql-server-ver15#installing-microsoft-odbc-driver-for-sql-server) versión 
 17.
 
**Driver Microsoft ODBC para SQL SERVER en Linux o MacOs**
 
Descargar e instalar el driver de la página [Microsoft ODBC](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/system-requirements?view=sql-server-ver15) versión 17 deacuerdo a la versión de su sistema operativo.
Recuerde estar conectado a la VPN para poder accerder. 

**Paquete pyobdc**

Quite el comentario e inicie la instalación simple.

## Cómo contribuir

En esta sección puede agregar los pasos metodológicos necesarios para publicar algún cambio en el proyecto. Por lo general, mantendremos la siguiente estructura:

1. Clona el repositorio.

2. Realiza los cambios necesarios en tu propia rama.

3. Envía una solicitud de extracción (pull request).

## Licencia

[Describa brevemente la licencia que usará para el proyecto]
