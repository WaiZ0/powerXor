# PowerXor
A script to bypass simple detection, no AMSI bypass included, do it yourself.

Inspired from FuckThatPacker, just python3.

# Basic usage

```
python3 powerXor.py -h                                 
usage: powerXor.py [-h] [-k KEY] [-o OUTPUT] file_path

Encode a PowerShell script file using XOR encryption and base64 encoding

positional arguments:
  file_path             Path to the PowerShell script file

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     XOR encryption key (default: randomly generated)
  -o OUTPUT, --output OUTPUT
                        Output file name (default: output.ps1)
```

# Exemple 
```
python3 powerXor.py test.ps1 -k 13 -o run.ps1          
[*] Reading the file ...
[*] Encoding the content (utf-16-le) ...
[*] Xoring with Key: 13
[*] Base64 encoding
[*] Writing to output file: run.ps1
[*] Process completed.
```
Can then be run on Windows.
