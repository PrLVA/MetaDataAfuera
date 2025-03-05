# Limpiador de Metadatos

Una herramienta en Python con interfaz gráfica para eliminar metadatos de imágenes (JPEG, PNG) y PDFs, diseñada para mejorar la privacidad al compartir archivos.

## Características
- **Soporte de formatos**: Elimina metadatos de archivos `.jpg`, `.jpeg`, `.png` y `.pdf`.
- **Interfaz gráfica**: Usa `tkinter` para una experiencia de usuario simple.
- **Procesamiento local**: Todo se realiza en tu máquina, sin necesidad de subir archivos a servicios en línea.
- **Resultados visibles**: Muestra el progreso y resultados en una ventana de texto.

## Requisitos
- Python 3.x
- Librerías:
  - `Pillow` (para imágenes)
  - `PyPDF2` (para PDFs)
  - `tkinter` (incluido con Python)

Instala las dependencias con:
```bash
pip install Pillow PyPDF2
