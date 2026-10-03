from datetime import datetime, timedelta
import keyboard
import pygame
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

pygame.mixer.init()
boolean = 1

athanmp3 = "Athan.mp3" # Athan file
duamp3 = "dua.mp3" # Dua File

text_folder = "Text_Files"
textfiles = os.listdir()

athanlength = (202) # Change Athan length (Seconds)
dualength = (14) # Change Dua length (Seconds)

def prayer_time():
    
    salah_time = datetime.now().strftime("%y-%m.txt %d %H:%M:%S")
    
    file_name, line, t = salah_time.split()
    
    year = file_name[0:2]
    month = file_name[3:5]
    date = line
    
    file_path = os.path.join(text_folder, file_name)
    
    with open(file_path, "r", encoding="UTF-8") as f:
        fajr = (f.readlines()[int(line)-1]).split(" ")[2]
   
    with open(file_path, "r", encoding="UTF-8") as f:
        dhuhr = (f.readlines()[int(line)-1]).split(" ")[4]
   
    with open(file_path, "r", encoding="UTF-8") as f:
        asr = (f.readlines()[int(line)-1]).split(" ")[5]
   
    with open(file_path, "r", encoding="UTF-8") as f:
        maghrib = (f.readlines()[int(line)-1]).split(" ")[6]
   
    with open(file_path, "r", encoding="UTF-8") as f:
        isha = (f.readlines()[int(line)-1]).split(" ")[7]
    
    fajr_obj = datetime.strptime(fajr, "%H:%M")
    fajr = fajr_obj.strftime("%H:%M:%S")
    
    witr_obj = fajr_obj - timedelta(minutes=15)
    witr = witr_obj.strftime("%H:%M:%S")
            
    dhuhr_obj = datetime.strptime(dhuhr, "%H:%M")
    dhuhr = dhuhr_obj.strftime("%H:%M:%S")
                    
    asr_obj = datetime.strptime(asr, "%H:%M")
    asr = asr_obj.strftime("%H:%M:%S")
                            
    maghrib_obj = datetime.strptime(maghrib, "%H:%M")
    maghrib = maghrib_obj.strftime("%H:%M:%S")
                                    
    isha = isha.strip()
    isha_obj = datetime.strptime(isha, "%H:%M")
    isha = isha_obj.strftime("%H:%M:%S")
    
    salah = (
        #f"{year}-{month} {date} {datetime.now().strftime("%H:%M:%S")}", # For testing Athan
        f"{year}-{month} {date} {fajr}", 
        f"{year}-{month} {date} {dhuhr}", 
        f"{year}-{month} {date} {asr}",
        f"{year}-{month} {date} {maghrib}",
        f"{year}-{month} {date} {isha}",
        f"{year}-{month} {date} {witr}"
        )
    
    return salah

def clock():
    
    while boolean == 1:
    
        current_time = datetime.now().strftime("%y-%m %d %H:%M:%S")
        print(current_time, prayer_time())
        
        if current_time in prayer_time():
            athan()    
            
        time.sleep(1)
        
def athan():
    
    pygame.mixer.music.load(athanmp3)
    pygame.mixer.music.play()
    
    time.sleep(athanlength)
    
    pygame.mixer.music.load(duamp3)
    pygame.mixer.music.play()
    
    time.sleep(dualength)
    
clock()