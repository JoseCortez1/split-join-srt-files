"""
Módulo para manejar la división de archivos SRT
"""

import os
from typing import List
from ..utils.file_handlers import ensure_directory

class SRTSplitter:
    def __init__(self, input_file: str):
        self.input_file = input_file
        
    def split(self, parts: int) -> List[str]:
        """
        Divide un archivo SRT en múltiples partes
        
        Args:
            parts (int): Número de partes en las que dividir el archivo
            
        Returns:
            List[str]: Lista de rutas de los archivos creados
        """
        # Leer el archivo
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Dividir en bloques
        blocks = content.strip().split('\n\n')
        subs_per_file = len(blocks) // parts
        
        # Crear directorio de salida
        output_dir = ensure_directory('split_files')
        output_files = []
        
        # Dividir y guardar
        base_name = os.path.splitext(os.path.basename(self.input_file))[0]
        
        for i in range(parts):
            start_idx = i * subs_per_file
            end_idx = start_idx + subs_per_file if i < parts-1 else len(blocks)
            
            part_content = '\n\n'.join(blocks[start_idx:end_idx])
            output_file = os.path.join(output_dir, f'{base_name}_part{i+1}.srt')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(part_content)
            
            output_files.append(output_file)
            
        return output_files