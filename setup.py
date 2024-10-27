from setuptools import setup, find_packages

setup(
    name="srt_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "srt_tools=main:main",
        ],
    },
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Herramienta para dividir y unir archivos SRT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="subtitles, srt, translation",
    url="https://github.com/tuusuario/srt_tools",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)