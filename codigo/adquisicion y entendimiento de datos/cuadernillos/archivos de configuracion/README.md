# Archivos de configuración

Pasos para configurar el inicio de sesión de la aplicación:

1. Crear un archivo en esta carpeta con el nombre "config.ini"
2. Una vez creado el archivo deberá escribir las siguientes líneas, configurandolas de acuerdo con la base a la que le esté apuntando.

```
[ConexionSQLServerReports]
server = <servidor donde se encuentra la base>
username = <usuario de sql>
password = <contraseña>

[ConexionSQLServerSandBox]
server = <servidor donde se encuentra la base>
username = <usuario de sql>
password = <contraseña>

[ConexionDatalake]
account_name = <nombre del contenedor>
sas_token = <token sas>
datalake_path = <datalake_path>
url_blob = <url del blob>
```