import subprocess
import os
import sys

# ANSI color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def human_readable_size(size_bytes):
    """Convert bytes to a human-readable MB string."""
    return f"{size_bytes / (1024 * 1024):.2f} MB"

def compress_pdf(input_path, output_path, quality="screen"):
    """
    Compress PDF using Ghostscript.
    quality: screen, ebook, printer, prepress, default
    """
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path,
    ]
    try:
        subprocess.run(gs_command, check=True)
        print(f"{GREEN}Compressed PDF saved as: {output_path}{RESET}")
        # Print file sizes
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        print(f"{CYAN}Original size:   {human_readable_size(original_size)}{RESET}")
        print(f"{CYAN}Compressed size: {human_readable_size(compressed_size)}{RESET}")
        reduction = 100 * (original_size - compressed_size) / original_size
        color = YELLOW if reduction >= 0 else RED
        print(f"{color}Reduction:       {reduction:.1f}%{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Ghostscript failed: {e}{RESET}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage: python main.py input.pdf [output.pdf]{RESET}")
        sys.exit(1)
    input_pdf = sys.argv[1]
    # Ensure 'compressed' folder exists
    compressed_folder = "compressed"
    os.makedirs(compressed_folder, exist_ok=True)
    # Determine output file name
    base_name = os.path.basename(input_pdf)
    output_pdf = (
        sys.argv[2]
        if len(sys.argv) > 2
        else os.path.join(compressed_folder, "compressed_" + base_name)
    )
    compress_pdf(input_pdf, output_pdf)
