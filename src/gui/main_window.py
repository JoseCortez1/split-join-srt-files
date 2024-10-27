import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil

class SRTSplitterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SRT Splitter & Merger")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Variables
        self.input_file = tk.StringVar()
        self.num_parts = tk.IntVar(value=2)
        self.output_dir = tk.StringVar()
        
        # Crear y configurar el estilo
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TFrame', padding=10)
        
        # Marco principal
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sección de división
        self.create_split_section(main_frame)
        
        # Separador
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=15)
        
        # Sección de unión
        self.create_merge_section(main_frame)
        
        # Barra de estado
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_split_section(self, parent):
        # Marco para división
        split_frame = ttk.LabelFrame(parent, text="Dividir archivo SRT", padding=10)
        split_frame.pack(fill='x', pady=5)
        
        # Selección de archivo
        ttk.Label(split_frame, text="Archivo SRT:").pack(anchor='w')
        file_frame = ttk.Frame(split_frame)
        file_frame.pack(fill='x', pady=5)
        
        ttk.Entry(file_frame, textvariable=self.input_file).pack(side='left', fill='x', expand=True)
        ttk.Button(file_frame, text="Examinar", command=self.browse_input_file).pack(side='right', padx=5)
        
        # Número de partes
        parts_frame = ttk.Frame(split_frame)
        parts_frame.pack(fill='x', pady=5)
        ttk.Label(parts_frame, text="Número de partes:").pack(side='left')
        ttk.Entry(parts_frame, textvariable=self.num_parts, width=5).pack(side='left', padx=5)
        
        # Botón dividir
        ttk.Button(split_frame, text="Dividir archivo", command=self.split_file).pack(pady=10)

    def create_merge_section(self, parent):
        # Marco para unión
        merge_frame = ttk.LabelFrame(parent, text="Unir archivos SRT", padding=10)
        merge_frame.pack(fill='x', pady=5)
        
        # Selección de directorio
        ttk.Label(merge_frame, text="Directorio con archivos SRT:").pack(anchor='w')
        dir_frame = ttk.Frame(merge_frame)
        dir_frame.pack(fill='x', pady=5)
        
        ttk.Entry(dir_frame, textvariable=self.output_dir).pack(side='left', fill='x', expand=True)
        ttk.Button(dir_frame, text="Examinar", command=self.browse_output_dir).pack(side='right', padx=5)
        
        # Botón unir
        ttk.Button(merge_frame, text="Unir archivos", command=self.merge_files).pack(pady=10)

    def browse_input_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Archivos SRT", "*.srt"), ("Todos los archivos", "*.*")]
        )
        if filename:
            self.input_file.set(filename)

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir.set(directory)

    def split_file(self):
        if not self.input_file.get():
            messagebox.showerror("Error", "Por favor seleccione un archivo SRT")
            return
            
        try:
            input_file = self.input_file.get()
            parts = self.num_parts.get()
            
            # Crear directorio para archivos divididos
            output_dir = "split_files"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Leer archivo
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Dividir en bloques
            blocks = content.strip().split('\n\n')
            subs_per_file = len(blocks) // parts
            
            # Crear archivos divididos
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            
            for i in range(parts):
                start_idx = i * subs_per_file
                end_idx = start_idx + subs_per_file if i < parts-1 else len(blocks)
                
                part_content = '\n\n'.join(blocks[start_idx:end_idx])
                output_file = f'{output_dir}/{base_name}_part{i+1}.srt'
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(part_content)
            
            self.status_var.set(f"Archivo dividido en {parts} partes exitosamente")
            messagebox.showinfo("Éxito", f"Archivo dividido en {parts} partes\nUbicación: {os.path.abspath(output_dir)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al dividir archivo: {str(e)}")

    def merge_files(self):
        if not self.output_dir.get():
            messagebox.showerror("Error", "Por favor seleccione el directorio con los archivos SRT")
            return
            
        try:
            directory = self.output_dir.get()
            output_file = filedialog.asksaveasfilename(
                defaultextension=".srt",
                filetypes=[("Archivos SRT", "*.srt"), ("Todos los archivos", "*.*")]
            )
            
            if not output_file:
                return
            
            # Obtener archivos .srt
            srt_files = sorted([f for f in os.listdir(directory) if f.endswith('.srt')])
            
            all_blocks = []
            counter = 1
            
            # Leer y procesar cada archivo
            for srt_file in srt_files:
                with open(os.path.join(directory, srt_file), 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                
                blocks = content.split('\n\n')
                
                # Ajustar números de subtítulos
                for block in blocks:
                    lines = block.split('\n')
                    lines[0] = str(counter)
                    all_blocks.append('\n'.join(lines))
                    counter += 1
            
            # Guardar archivo final
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(all_blocks))
            
            self.status_var.set("Archivos unidos exitosamente")
            messagebox.showinfo("Éxito", f"Archivos unidos exitosamente\nArchivo guardado: {output_file}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al unir archivos: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SRTSplitterGUI(root)
    root.mainloop()