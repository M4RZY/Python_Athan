import os

os.chdir("Calendars")

for cal in os.listdir():
    file_name, file_type = os.path.splitext(cal)
    
    place, hyphen, month , year = file_name.split(' ')
    
    hyphen = hyphen.strip()
    
    year = year[2:]
    
    if month == "January":
        month = "01"
        
    elif month == "February":
        month = "02"
        
    elif month == "March":
        month = "03"
    
    elif month == "April":
        month = "04"
        
    elif month == "May":
        month = "05"
        
    elif month == "June":
        month = "06"
        
    elif month == "July":
        month = "07"
        
    elif month == "August":
        month = "08"
        
    elif month == "September":
        month = "09"
        
    elif month == "October":
        month = 10
        
    elif month == "November":
        month = 11
        
    elif month == "December":
        month = 12
    
    new_name = "{}-{}{}".format(year, month, file_type)
    
    os.rename(cal, new_name)