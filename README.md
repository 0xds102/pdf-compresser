# PDF Compressor (Python + Ghostscript)

A simple Python script to compress PDF files using [Ghostscript](https://www.ghostscript.com/).

---

## Features

- Compresses PDFs with images using Ghostscript for maximum size reduction.
- Automatically saves compressed files in a `compressed` folder.
- Shows original size, compressed size, and percentage reduction.

---

## Requirements

- **Python 3**
- **Ghostscript** installed and available in your system PATH.

### Install Ghostscript
- **macOS:**
  ```bash
  brew install ghostscript
  ```

### Usage

```bash
python3 main.py [filename.pdf]
```
```