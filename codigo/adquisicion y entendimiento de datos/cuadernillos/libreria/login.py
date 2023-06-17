import configparser
from configparser import ExtendedInterpolation
import pyodbc
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from enum import Enum

# Cargue de las credenciales para acceso a SQL server y/o a el DataLake
config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
config.read("archivos de configuracion/config.ini")

# Llaves para conexion a SQL server bodega
server_bodega = config.get('ConexionSQLServerReports', 'server')
username_bodega = config.get('ConexionSQLServerReports', 'username')
password_bodega = config.get('ConexionSQLServerReports', 'password')

# Llaves para conexion a SQL server SandBox
server_sandbox = config.get('ConexionSQLServerSandBox', 'server')
username_sandbox = config.get('ConexionSQLServerSandBox', 'username')
password_sandbox = config.get('ConexionSQLServerSandBox', 'password')

# Llaves para conexión al DataLake
account_name = config.get('ConexionDatalake', 'account_name')
sas_token = config.get('ConexionDatalake', 'sas_token')
datalake_path = config.get('ConexionDatalake', 'datalake_path')
url_blob = config.get('ConexionDatalake', 'url_blob')

class tipo_bodega(Enum):
    REPORTS = 1
    SANDBOX = 2

class cliente_contenedor(Enum):
    datosemae = 'datosemae'

def login_sql(bodega):
    '''
    Crea el cliente SQL para ejecutar consultas sobre la bodega (CCREPORTS o SANDBOX)

    Parámetros:
    bodega: Nombre de la bodega

    Retorna:
    cnxn, cursor
    '''
    if bodega == tipo_bodega.REPORTS:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_bodega+';UID='+username_bodega+';PWD='+ password_bodega)
    elif bodega == tipo_bodega.SANDBOX:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_sandbox+';UID='+username_sandbox+';PWD='+ password_sandbox)
    else:
        print("Debe ingresar un tipo de bodega valido")
        return None
    cursor = cnxn.cursor()
    return cnxn, cursor

def login_datalake(contenedor=cliente_contenedor.datosemae):
    '''
    Conexión a la cuenta de almacenamiento de Azure utilizando el token SAS, junto con el contenedor

    Parámetros:
    contenedor: Cliente contenedor. Por defecto es "datosemae"

    Retorna:
    blob_service_client, container_client
    '''
    connect_str = f"BlobEndpoint={url_blob};SharedAccessSignature={sas_token}"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(contenedor)
    return blob_service_client, container_client