## Proyecto generador de query SQL

### Descripción:

Programa para generar queries de inserción SQL por medio de archivos Excel y CSV

### Crear entorno virtual

Para crear un entorno virtual se debe ejecutar los siguientes comandos:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### Archivo de configuración JSON

Para cargar los datos de configuración JSON se debe hacer con la siguiente estructura:

```json
{
  "sheet_name": "NombreDeLaHoja",
  "table_name": "NombreDeLaTabla",
  "fields": {
    "nombreColumna1": "nombreColumna1Query",
    "nombreColumna2": "nombreColumna2Query"
  },
  "exclude_quotes": ["nombreColumna2"]
}
```

### Ejecución del programa

Para ejecutar el programa, ejecuta el siguiente comando:

```bash
python main.py
```

### Generar ejecutable

Para generar el ejecutable del programa, ejecuta el siguiente comando:

```bash
pyinstaller --onefile --windowed main.py
```