import pandas as pd

# Función para leer el archivo Excel
def read_excel(file_path, sheet_name):
  return pd.read_excel(file_path, sheet_name=sheet_name)

# Función para leer el archivo CSV
def read_csv(file_path):
  return pd.read_csv(file_path)

# Función para crear una query de inserción
def create_insert_query(table_name=None, fields=None, exclude_quotes=None, df=None):
  if df is None:
    raise ValueError("Se debe proporcionar un DataFrame")

  values = fields.values()
  keys = fields.keys()

  query = f'INSERT INTO `{table_name}` ('
  for value in values:
    query += f'`{value}`, '

  query = query[:-2] + ') VALUES \n('

  for index, row in df.iterrows():
    for key in keys:
      # Si el valor es nulo, se inserta NULL
      if pd.isnull(row[key]):
        query += 'NULL, '
      # Si el campo no tiene comillas, se inserta sin comillas
      elif key in exclude_quotes:
        query += f'{row[key]}, '
      else:
        query += f'"{row[key]}", '

    query = query[:-2] + '), \n('

  query = query[:-4] + ';'
  return query
