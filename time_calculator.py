#def add_time(start, duration):


def add_time(startTime,increaseTime,startDay=""):
    
    increaseDay = 0
    dayNumber = 0

    startFullHour = startTime.split(' ')[0]
    startM = startTime.split(' ')[1]
    startHour = int(startFullHour.split(':')[0])
    startMinute = int(startFullHour.split(':')[1])
    
    increaseHour=int(increaseTime.split(':')[0])
    increaseMinute=int(increaseTime.split(':')[1])

    
    totalMinute = (startMinute+increaseMinute)%60
    totalHours = (startHour+increaseHour+int((startMinute+increaseMinute)/60))%12
    increaseDay += int((startHour+increaseHour+int((startMinute+increaseMinute)/60))/24)
   
    if(totalHours==0):
        totalHours = 12
    
    if(startHour+(increaseHour%24+int((startMinute+increaseMinute)/60)) >= 12):
        if(startM =="AM"):
            startM = "PM"
        else:
            startM = "AM"
            increaseDay+=1


    finalResult = str(totalHours)+":"
    if(totalMinute<10):
        finalResult+="0"
    finalResult+=str(totalMinute)+" "
    finalResult+=startM 

    if(startDay and increaseDay>=1):
        startDay = startDay.lower()

        if(startDay == "monday"):
            dayNumber = 0
        if(startDay == "tuesday"):
            dayNumber = 1
        if(startDay == "wednesday"):
            dayNumber = 2
        if(startDay == "thursday"):
            dayNumber = 3
        if(startDay == "friday"):
            dayNumber = 4
        if(startDay == "saturday"):
            dayNumber = 5
        if(startDay == "sunday"):
            dayNumber = 6

        
        dayNumber = (dayNumber + increaseDay%7 )%7
       
        
        if(dayNumber == 0):
            startDay = "monday"
        if(dayNumber == 1):
            startDay = "tuesday"
        if(dayNumber == 2):
            startDay = "wednesday"
        if(dayNumber == 3):
            startDay = "thursday"
        if(dayNumber == 4):
            startDay = "friday"
        if(dayNumber == 5):
            startDay = "saturday"
        if(dayNumber == 6):
            startDay = "sunday" 


    startDay = startDay.capitalize()

    if(startDay):
        finalResult+=", "+startDay

    if(increaseDay==1):
        finalResult+=" "+"(next day)"
    if(increaseDay>1):
        finalResult+=" ("+str(increaseDay)+" days later)"  
  


    return finalResult