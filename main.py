#!/usr/bin/env python3
"""
SRT Tools - Herramienta para manipular archivos de subtítulos
"""

import sys
from src.gui.main_window import SRTToolsGUI
from tkinter import Tk

def main():
    """Punto de entrada principal de la aplicación"""
    root = Tk()
    app = SRTToolsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()