import os

text_folder = "Text Files"

os.chdir(text_folder)
textfiles = os.listdir()
    
for file in textfiles:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        newlines = lines[3:-1]
        
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(newlines)

print("Done")