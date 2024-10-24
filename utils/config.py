import json

# Función para cargar la configuración desde un archivo JSON
def load_config(config_path):
  with open(config_path, 'r') as file:
    config = json.load(file)
  return config

# Función para validar la estructura del JSON
def validate_json_structure(data):
  # Definir la estructura esperada
  expected_structure = {
    "sheet_name": str,
    "table_name": str,
    "fields": dict,
    "exclude_quotes": list
  }
  
  # Validar cada campo
  for key, expected_type in expected_structure.items():
    if key not in data:
      raise ValueError(f"Falta la clave '{key}' en el JSON.")
    
    if not isinstance(data[key], expected_type):
      raise TypeError(f"La clave '{key}' debe ser de tipo {expected_type.__name__}.")

  # Validar que 'fields' sea un diccionario con las claves y valores correctos
  for field_key, field_value in data["fields"].items():
    if not isinstance(field_key, str) or not isinstance(field_value, str):
      raise TypeError(f"Las claves y valores en 'fields' deben ser de tipo str.")

   # Validar que 'exclude_quotes' contenga claves válidas de 'fields'
  for exclude in data["exclude_quotes"]:
    if exclude not in data["fields"]:
      raise ValueError(f"'{exclude}' no es una clave válida en 'fields'.")

  return True  # La estructura es válida
