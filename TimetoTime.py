import os
from datetime import datetime

text_folder = "Text Files"
os.chdir(text_folder)

textfiles = os.listdir()

for file in textfiles:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        day, date, fajr, sunrise, dhuhr, asr, maghrib, isha = line.split(" ")
        
        fajr_obj = datetime.strptime(fajr, "%H:%M")
        fajr = fajr_obj.strftime("%H:%M:%S")
        
        dhuhr_obj = datetime.strptime(dhuhr, "%H:%M")
        dhuhr = dhuhr_obj.strftime("%H:%M:%S")
                
        asr_obj = datetime.strptime(asr, "%H:%M")
        asr = asr_obj.strftime("%H:%M:%S")
                        
        maghrib_obj = datetime.strptime(maghrib, "%H:%M")
        maghrib = maghrib_obj.strftime("%H:%M:%S")
                                
        isha = isha.strip()
        isha_obj = datetime.strptime(isha, "%H:%M")
        isha = isha_obj.strftime("%H:%M:%S")
        
        print(fajr, dhuhr, asr, maghrib, isha)