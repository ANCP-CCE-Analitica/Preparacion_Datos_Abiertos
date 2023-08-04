# Librerías base
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import os as os

# ====================
# Organizar para presentación
from IPython.display import HTML
from IPython.display import Markdown as md

# ====================
# Lectrua SQL
import pyodbc

# ====================
# Text processing
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ====================
# Hash
import hashlib

# ====================
# Warnings
import warnings
warnings.filterwarnings('ignore')

# ====================
# Mappings
import plotly.express as px
import plotly.io as pio

from urllib.request import urlopen
import json
url='https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/3aadedf47badbdac823b00dbe259f6bc6d9e1899/colombia.geo.json'
with urlopen(url) as response:
    colombia_map= json.load(response)
    
################################
## Funciones de limpieza #######
################################

# Limpieza del objeto contractual
# ==============================================================================
stop_words = set(stopwords.words("spanish"))

# Función Limpieza de Texto
def remove_extra_punct(text):
    
    text = text.lower()
    text = re.sub(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', "", text)
    text = re.sub(r'[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]', "", text)
    text = re.sub(r'\#\.', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'  ', ' ', text)
    text = re.sub(r'´', '',text)
    text = re.sub(r',', '',text)
    text = re.sub(r'\-', '', text)
    text = re.sub(r'á', 'a', text)
    text = re.sub(r'é', 'e', text)
    text = re.sub(r'í', 'i', text)
    text = re.sub(r'ó', 'o', text)
    text = re.sub(r'ú', 'u', text)
    text = re.sub(r'ò', 'o', text)
    text = re.sub(r'à', 'a', text)
    text = re.sub(r'è', 'e', text)
    text = re.sub(r'ì', 'i', text)
    text = re.sub(r'ù', 'u', text)
    text = re.sub("\d+", ' ', text)
    text = re.sub("\\s+", ' ', text)
    
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if not w.lower() in stop_words]
    tokens = " ".join(tokens)
    
    return tokens

# Arreglo de modalidades
# ==============================================================================
def Tipo_Proceso (mod):
    if (mod == "Asociacion Publico Privada") | (mod == "Asociación Público Privada"):
        tp = "Asociación Público Privada"
    elif (mod == "Concurso de meritos abierto") | (mod == "Concurso de Méritos con Lista Corta") | (mod == "Concurso de méritos abierto") | (mod == "Concurso de Méritos Abierto") | (mod == "CCE-20-Concurso_Meritos_Sin_Lista_Corta_1Sobre") | (mod == "Concurso de meritos con precalificacion") | (mod == "Concurso de Meritos con Lista Corta") | (mod == "Concurso de Meritos Abierto") | (mod == "Concurso de diseño Arquitectónico"):
        tp = "Concurso de Méritos"
    elif (mod  == "Contratacion directa") | (mod == "Contratación Directa (con ofertas)") | (mod == "Contratación directa") | (mod == "Contratacion Directa (con ofertas)") | (mod == "Contratacion Directa (Ley 1150 de 2007)") | (mod == "Contratación Directa (Ley 1150 de 2007)"):
        tp = "Contratación Directa"
    elif (mod == "Minima cuantia") | (mod == "Mínima cuantía") | (mod == "Contratacion Minima Cuantia") | (mod == "Contratación Mínima Cuantía"):
        tp = "Contratación Mínima Cuantía"
    elif (mod == "Contratos y convenios con mas de dos partes") | (mod == "Contratos y convenios con más de dos partes"):
        tp = "Convenios dos Partes"
    elif (mod == "Licitacion publica") | (mod == "Licitación pública Obra Publica") | (mod == "Licitacion publica Obra Publica") | (mod == "Licitación Pública") | (mod == "Licitación obra pública") | (mod == "Licitacion obra publica") | (mod == "Licitacion Publica") | (mod == "Licitación pública"):
        tp = "Licitación Pública"
    elif (mod == "Licitacion Publica Acuerdo Marco de Precios") | (mod == "Licitación Pública Acuerdo Marco de Precios"):
        tp = "Licitacion Publica Acuerdo Marco de Precios"
    elif (mod == "Contratacion regimen especial") | (mod == "Contratación régimen especial (con ofertas)") | (mod == "Contratación régimen especial") | (mod == "Régimen Especial") | (mod == "Contratacion regimen especial (con ofertas)") | (mod == "Regimen Especial"):
        tp = "Régimen Especial"
    elif (mod == "Enajenacion de bienes con sobre cerrado") | (mod == "Enajenacion de bienes con subasta") | (mod == "Enajenación de bienes con subasta") | (mod == "Enajenación de bienes con sobre cerrado"):
        tp = "Enajenacion de bienes"
    elif (mod == "Seleccion Abreviada de Menor Cuantia") | (mod == "Selección Abreviada del literal h del numeral 2 del artículo 2 de la Ley 1150 de 2007") | (mod == "Subasta") | (mod == "Selección abreviada subasta inversa") | (mod == "Selección Abreviada servicios de Salud") | (mod == "Selección Abreviada de Menor Cuantía") | (mod == "Selección Abreviada de Menor Cuantía (Ley 1150 de 2007)") | (mod == "Seleccion Abreviada Menor Cuantia Sin Manifestacion Interes") | (mod == "Seleccion abreviada subasta inversa") | (mod == "Seleccion Abreviada de Menor Cuantia (Ley 1150 de 2007)") | (mod == "Seleccion Abreviada del literal h del numeral 2 del articulo 2 de la Ley 1150 de 2007") | (mod == "Seleccion Abreviada servicios de Salud"):
        tp = "Selección Abreviada"
    else:
        tp = "Otras Modalidades de Contratación"
        
    return tp

def Grupo_Modalidad (mod):
    if (mod == "Contratación Directa"):
        gm = "Modalidad Directa"
    elif (mod == "Licitación Pública") | (mod == "Enajenacion de bienes") | (mod == "Licitacion Publica AMP") | (mod == "Concurso de Méritos") | (mod == "Contratación Mínima Cuantía") | (mod == "Selección Abreviada") | (mod == "Subasta")| (mod == "Licitacion Publica Acuerdo Marco de Precios"):
        gm = "Modalidad Competitiva"
    elif (mod == "Régimen Especial") | (mod == "Asociación Público Privada") | (mod == "Convenios dos Partes"):
        gm = "Modalidad Especial"
    else:
        gm = "Otra Modalidad"
    return gm

def eliminar_nulos(df, nombre_columna):
    '''Elimina nulos de una columna específica'''
    df = df.dropna(subset=[nombre_columna])
    return df

def limpiar_texto(df, nombre_columna):
    '''Limpia el texto de una columna específica'''
    df[nombre_columna + ' limpio'] = df[nombre_columna].apply(remove_extra_punct)
    return df

def datos_filtro_palabras(df, nombre_columna, lista_palabras):
    '''Genera un dataframe con los datos que contengan las palabras de la lista'''
    df_result = df[df[nombre_columna].str.contains('|'.join(lista_palabras), case=False, na=False)]
    return df_result

def eliminar_duplicados(df, nombre_columna):
    '''Elimina duplicados de una columna específica'''
    df = df.drop_duplicates(subset=[nombre_columna], keep='first')
    return df

def mayuscula(df, nombre_columna):
    '''Convertir todo en mayúscula de una columna específica'''
    df[nombre_columna] = df[nombre_columna].str.upper()
    return df[nombre_columna]

def formato_oracion(df, nombre_columna):
    '''Convertir el texto en formato de tipo oración de una columna específica'''
    df[nombre_columna] = df[nombre_columna].str.capitalize()
    return df[nombre_columna]

# Limpieza de códigos UNSPSC
def limpieza_codigos_unspsc(df,nombre_columna):

    df[nombre_columna]=df[nombre_columna].astype(str)
    codigos_limpios = []
    alertas_unspc = []
    for codigo in df[nombre_columna]:
        codigo_limpio = re.sub('[^0-9]', '', codigo)
        
        if len(codigo_limpio) ==6:
            codigos_limpios.append(codigo_limpio+'00')
            alertas_unspc.append(False)
        elif len(codigo_limpio) ==9:
            codigos_limpios.append(codigo_limpio[1:])
            alertas_unspc.append(False)
        elif len(codigo_limpio) !=8:
            codigos_limpios.append(codigo_limpio)
            alertas_unspc.append(True)
        else:
            codigos_limpios.append(codigo_limpio)
            alertas_unspc.append(False)

    df[nombre_columna]=codigos_limpios
    df['Alerta UNSPSC']=alertas_unspc
    
    return df





################################
## Otras funciones #############
################################


def generate_hash_key(string):
    # Codifica la cadena en formato de bytes
    encoded_string = string.encode('utf-8')
    
    # Genera el hash SHA256 de la cadena codificada
    hash_obj = hashlib.sha256(encoded_string)
    hash_digest = hash_obj.digest()
    
    # Convierte el hash digest a una cadena hexadecimal
    hex_digest = hash_digest.hex()
    

    return hex_digest.upper()

