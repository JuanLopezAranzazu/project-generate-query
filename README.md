## Proyecto Query Excel

### Descripción:

Programa para leer archivos excel y generar queries para insertar datos SQL

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
  "table_name": "nombre_tabla",
  "fields": {
    "columna1": "campo1",
    "columna2": "campo2",
    "columna3": "campo3"
  },
  "exclude_quotes": ["columna3"]
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