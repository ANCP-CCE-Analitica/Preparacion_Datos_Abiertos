# Data_Acquisition_and_Understanding

Esta carpeta alberga código para la adquisición y comprensión de datos (análisis exploratorio). 

## Acceso a las fuentes de datos de la agencia

Para acceder a las fuentes de datos disponibles de la agencia, sigue los pasos a continuación:

### Configuración de las credenciales 

1. Abre el archivo [config.ini](./Archivos%20de%20configuracion/config.ini).
2. Proporciona las credenciales necesarias en el archivo [config.ini](./Archivos%20de%20configuracion/config.ini) según la fuente que se deseas consultar. Asegúrate de completar todos los campos requeridos, como el nombre de usuario y la contraseña.

### Acceso a la bodega (reports o sandbox)

1. Importa el archivo [login.py](./Notebooks/login.py) en tu cuaderno o script Python (recuerda que debe ir ubicado en alguna de las carpetas preestablecidas):

```ìmport login```

2. Asegurate de tener activa la conexión a la VPN.

3. Llama a la función login_sql() y configura la bodega a la que deseas acceder (reports o sandbox):

```
cnxn, cursor = login.login_sql(login.tipo_bodega.REPORTS)  # Para la bodega reports
cnxn, cursor = login.login_sql(login.tipo_bodega.SANDBOX)  # Para la bodega sandbox

# Ejemplo de consulta en Bodega de Datos
# ==============================================================================

import pandas as pd
query = '''

select top 10 * 
from NombreBase.NombreTabla
'''

df = pd.read_sql(query, con=cnxn)
print(df.shape)
```

Esta función se encargará de realizar el proceso de inicio de sesión en las bodegas de datos de la agencia. 

### Acceso al datalake

1. Importa el archivo login.py en tu cuaderno o script Python:

```ìmport login```

2. Llama a la función login_datalake() y configura el contenedor del cual extraeras los datos (por defecto es datosemae):

```blob_service_client, container_client = login.login_datalake(login.cliente_contenedor.datosemae)

import pandas as pd

# Obtener el archivo
blob_client = blob_service_client.get_blob_client(container='name_blob', blob='ruta_file')

# Usar pandas para leer el archivo
df = pd.read_csv(blob_client.download_blob())

# Mostrar los datos
display(df.head())
```