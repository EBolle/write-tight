import sys 
from pathlib import Path

def get_text_file() -> str:

    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    else:
        print("Please provide a path to the text file.")
        return
    
    if Path(input_file_path).exists():
        input_file_path_abs = Path(input_file_path).absolute()
        with open(input_file_path_abs, encoding="utf-8") as input_stream:
            input_file = input_stream.read()
        return input_file
    else:
        print("The path does not exist.")
        return
