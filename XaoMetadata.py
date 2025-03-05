import os
from PIL import Image
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para eliminar metadatos de imágenes
def remove_image_metadata(input_path, output_path):
    try:
        img = Image.open(input_path)
        data = list(img.getdata())
        img_no_metadata = Image.new(img.mode, img.size)
        img_no_metadata.putdata(data)
        img_no_metadata.save(output_path)
        return True, f"Metadatos eliminados de {input_path}"
    except Exception as e:
        return False, f"Error procesando {input_path}: {str(e)}"

# Función para eliminar metadatos de PDFs
def remove_pdf_metadata(input_path, output_path):
    try:
        with open(input_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            for page in pdf.pages:
                writer.add_page(page)
            writer.add_metadata({"/Producer": "Anonimizado", "/CreationDate": None})
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
        return True, f"Metadatos eliminados de {input_path}"
    except Exception as e:
        return False, f"Error procesando {input_path}: {str(e)}"

# Función para procesar el archivo
def clean_metadata(input_path, output_dir="cleaned_files"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_cleaned{ext}")
    
    if ext.lower() in ['.jpg', '.jpeg', '.png']:
        success, message = remove_image_metadata(input_path, output_path)
    elif ext.lower() == '.pdf':
        success, message = remove_pdf_metadata(input_path, output_path)
    else:
        success, message = False, f"Formato no soportado: {ext}"
    
    return success, message

# Interfaz gráfica
class MetadataCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Limpiador de Metadatos")
        self.root.geometry("400x300")
        
        # Etiqueta
        self.label = tk.Label(root, text="Selecciona un archivo para limpiar metadatos", pady=10)
        self.label.pack()
        
        # Botón para seleccionar archivo
        self.select_button = tk.Button(root, text="Seleccionar archivo", command=self.select_file)
        self.select_button.pack(pady=5)
        
        # Área de texto para mostrar resultados
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)
        
        # Botón para limpiar
        self.clean_button = tk.Button(root, text="Limpiar Metadatos", command=self.clean_file, state="disabled")
        self.clean_button.pack(pady=5)
        
        self.file_path = None
    
    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Archivos soportados", "*.jpg *.jpeg *.png *.pdf"), ("Todos los archivos", "*.*")]
        )
        if self.file_path:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Archivo seleccionado: {self.file_path}\n")
            self.clean_button.config(state="normal")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "No se seleccionó ningún archivo.\n")
            self.clean_button.config(state="disabled")
    
    def clean_file(self):
        if self.file_path:
            success, message = clean_metadata(self.file_path)
            self.result_text.insert(tk.END, message + "\n")
            if success:
                messagebox.showinfo("Éxito", "Metadatos limpiados correctamente.")
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo primero.")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MetadataCleanerApp(root)
    root.mainloop()