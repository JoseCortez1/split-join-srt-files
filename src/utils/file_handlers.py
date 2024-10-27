"""
Utilidades para el manejo de archivos
"""

import os
from typing import Optional

def ensure_directory(path: str) -> str:
    """
    Asegura que un directorio existe, creándolo si es necesario
    
    Args:
        path (str): Ruta del directorio
        
    Returns:
        str: Ruta absoluta del directorio
    """
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)

def get_srt_files(directory: str) -> list:
    """
    Obtiene todos los archivos .srt en un directorio
    
    Args:
        directory (str): Directorio a escanear
        
    Returns:
        list: Lista de archivos .srt encontrados
    """
    return sorted([
        f for f in os.listdir(directory)
        if f.lower().endswith('.srt')
    ])

def safe_read_file(file_path: str, encoding: str = 'utf-8') -> Optional[str]:
    """
    Lee un archivo de forma segura
    
    Args:
        file_path (str): Ruta del archivo
        encoding (str): Codificación del archivo
        
    Returns:
        Optional[str]: Contenido del archivo o None si hay error
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"Error leyendo {file_path}: {e}")
        return None