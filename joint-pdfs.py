import os
import platform
import subprocess
import tkinter as tk
from tkinter import filedialog

from pikepdf import Pdf


# Função para combinar PDFs
def combine_pdfs(pdf_files):
    output_pdf = Pdf.new()

    for pdf in pdf_files:
        with Pdf.open(pdf) as src_pdf:
            for page in src_pdf.pages:
                output_pdf.pages.append(page)

    combined_pdf_name = "combined.pdf"
    output_pdf.save(combined_pdf_name)

    return combined_pdf_name


# Função para abrir uma janela de seleção de arquivos
def select_files():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Abrir a janela de diálogo para seleção de arquivos
    file_paths = filedialog.askopenfilenames(
        title="Selecione os arquivos PDF", filetypes=[("Arquivos PDF", "*.pdf")]
    )

    return list(file_paths)


# Função para abrir o arquivo PDF combinado
def open_file(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", file_path])
    else:  # Linux
        subprocess.run(["xdg-open", file_path])


# Selecionar arquivos PDF
pdf_files = select_files()

if pdf_files:
    # Combinar PDFs
    combined_pdf_name = combine_pdfs(pdf_files)

    # Confirmar a criação do PDF combinado
    print(f'PDF combinado salvo como "{combined_pdf_name}"')

    # Abrir o PDF combinado automaticamente
    open_file(combined_pdf_name)
else:
    print("Nenhum arquivo PDF selecionado.")
