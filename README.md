# SRT Tools

SRT Tools is a simple yet powerful desktop application for manipulating subtitle files (.srt). Specifically designed to facilitate the subtitle translation process by splitting large files into more manageable parts.

## 🚀 Features

- **File Splitting**: Split large SRT files into smaller parts
- **File Merging**: Merge multiple SRT files into one
- **Graphical Interface**: Intuitive and easy-to-use interface
- **Format Preservation**: Maintains correct subtitle numbering and formatting
- **Unicode Support**: Full support for special characters and different languages

## 📋 Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes with Python)

## 🔧 Installation

1. Clone or download this repository
```bash
git clone https://github.com/your-username/srt-tools.git
cd srt-tools
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
```bash
# On Windows
.\venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the application:
```bash
python main.py
```

2. To split a file:
    - Click "Browse" and select your SRT file
    - Specify the desired number of parts
    - Click "Split file"

3. To merge files:
    - Select the folder containing the translated SRT files
    - Click "Merge files"
    - Choose where to save the final file

## 📁 Project Structure

```
srt_tools/
├── src/
│   ├── core/        # Core logic
│   ├── gui/         # Graphical interface
│   └── utils/       # Utilities
├── tests/           # Tests
├── docs/            # Documentation
└── resources/       # Resources (icons, etc.)
```

## 🤝 Contributing

Contributions are welcome:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Your Name - [JoseCortez1](https://github.com/JoseCortez1) - jose.vazcortez@gmail.com

Project Link: [https://github.com/JoseCortez1/split-join-srt-files](https://github.com/JoseCortez1/split-join-srt-files)