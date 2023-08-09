from pathlib import Path
import sys

input_file = Path(sys.argv[1]).read_text()
input_file = input_file.replace("=", ",")
input_file = input_file.replace(" AND ", " & ")
input_file = input_file.replace(" OR ", " | ")
input_file = input_file.replace("NOT ", "!")
print("targets,factors")
print(input_file)