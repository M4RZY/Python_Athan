import os

text_folder = "Text Files"
os.chdir(text_folder)

textfiles = os.listdir()
#for file in textfiles:
with open(textfiles[0], "r", encoding="utf-8") as f:
    lines = f.readlines()
        #filename, filetype = os.path.splitext(file)
        #print(filename)
    
    for line in lines:
        day, date, fajr, sunrise, dhuhr, asr, maghrib, isha = line.split(" ")
        print(fajr)