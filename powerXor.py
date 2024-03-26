#!/usr/bin/env python3

import argparse
import base64
import random
from pathlib import Path

"""
Exemple: python3 powerXor.py test.ps1 -k 13 -o run.ps1
"""

def xor_encrypt(data, key):
    return bytes([b ^ key for b in data])

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Encode a PowerShell script file using XOR encryption and base64 encoding")
    parser.add_argument("file_path", type=Path, help="Path to the PowerShell script file")
    parser.add_argument("-k", "--key", type=int, help="XOR encryption key (default: randomly generated)")
    parser.add_argument("-o", "--output", type=Path, help="Output file name (default: output.ps1)")
    args = parser.parse_args()

    # Read the content of the file
    print(f"[*] Reading the file ...")
    with args.file_path.open('r', encoding='utf-8') as file:
        script_content = file.read()

    # Encode the content into UTF-16-LE
    print(f"[*] Encoding the content (utf-16-le) ...")
    encoded_content = script_content.encode('utf-16-le')
    

    # Generate or use provided key
    if args.key is None:
        key = random.randint(0, 255)
    else:
        key = args.key
    

    # XOR encrypt the content
    print(f"[*] Xoring with Key: {key}")
    encrypted_content = xor_encrypt(encoded_content, key)

    # Base64 encode the result
    print(f"[*] Base64 encoding")
    encoded_result = base64.b64encode(encrypted_content).decode('utf-8')

    # Prepare output content
    output_content = ""
    template_path = Path("template.ps1")
    with template_path.open('r', encoding='utf-8') as template_file:
        output_content = template_file.read().replace("%%KEY%%", str(key)).replace("%%DATA%%", encoded_result)

    # Write to output file
    output_file = args.output if args.output else Path("output.ps1")
    print(f"[*] Writing to output file: {output_file}")
    with output_file.open('w', encoding='utf-8') as output:
        output.write(output_content)

    print("[*] Process completed.")

if __name__ == "__main__":
    main()
