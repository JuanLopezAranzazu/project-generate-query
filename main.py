import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils.create_query import read_excel, create_insert_query
from utils.get_config import load_config

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Proyecto Query Excel")
    self.root.geometry("750x500")

    # Cargar la configuración
    self.config = {}

    self.create_widgets()

  def create_widgets(self):
    # Crear el marco para la columna de formulario
    self.frame_form = ttk.Frame(self.root, padding="10")
    self.frame_form.grid(row=0, column=0, sticky="nsew")

    # Crear elementos del formulario
    # Botón para seleccionar el archivo de configuración JSON
    self.select_file_button = ttk.Button(self.frame_form, text="Seleccionar Archivo", command=self.on_select_file)
    self.select_file_button.grid(row=0, column=0, sticky="ew", pady=5)

    # Botón para seleccionar el archivo
    self.create_query_button = ttk.Button(self.frame_form, text="Crear Query", command=self.on_create_query)
    self.create_query_button.grid(row=1, column=0, sticky="ew", pady=5)

    # Botón para limpiar el campo de resultados
    self.clear_button = ttk.Button(self.frame_form, text="Limpiar", command=lambda: self.text_results.delete("1.0", tk.END))
    self.clear_button.grid(row=2, column=0, sticky="ew", pady=5)

    # Crear el marco para la columna de resultados
    self.frame_results = ttk.Frame(self.root, padding="10")
    self.frame_results.grid(row=0, column=1, sticky="nsew")

    # Crear elementos de resultados
    self.text_results = tk.Text(self.frame_results, height=30, width=50)
    self.text_results.grid(row=0, column=0, sticky="nsew")

    # Configurar el frame_form para expandirse en ambas direcciones
    self.frame_form.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Configurar el frame_results para expandirse en ambas direcciones
    self.frame_results.grid_rowconfigure(0, weight=1)  # Permitir crecimiento vertical
    self.frame_results.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Ajustar el peso de las columnas
    self.root.grid_columnconfigure(0, weight=1)  # Columna del formulario
    self.root.grid_columnconfigure(1, weight=1)  # Columna de resultados

    # Ajustar el peso de las filas
    self.root.grid_rowconfigure(0, weight=1)  # Fila principal

  def on_select_file(self):
    # Seleccionar el archivo de configuración JSON
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

    if not file_path:
      return

    try:
      self.config = load_config(file_path)
      messagebox.showinfo("Información", f"Se ha cargado el archivo {file_path} con éxito")
    except Exception as e:
      messagebox.showerror("Error", str(e))

  def on_create_query(self):
    # Seleccionar el archivo de Excel
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    if not file_path:
      return

    try:
      # Obtener los valores de la configuración
      SHEET_NAME = self.config.get("sheet_name")
      TABLE_NAME = self.config.get("table_name")
      FIELDS = self.config.get("fields")
      EXCLUDE_QUOTES = self.config.get("exclude_quotes")
      # Leer el archivo de Excel
      df = read_excel(file_path, sheet_name=SHEET_NAME)
      query = create_insert_query(TABLE_NAME, FIELDS, EXCLUDE_QUOTES, df=df)
      self.text_results.delete("1.0", tk.END)
      self.text_results.insert(tk.END, query)
    except Exception as e:
      messagebox.showerror("Error", str(e))

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()