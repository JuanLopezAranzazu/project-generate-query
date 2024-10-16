import json

# Función para cargar la configuración desde un archivo JSON
def load_config(config_path):
  with open(config_path, 'r') as file:
    config = json.load(file)
  return config
