import pyperclip

while True:
    hours = raw_input("Hours: ")
    if( hours == -1):
        exit()
    minutes = raw_input("Minutes: ")
    seconds = raw_input("Seconds: ")

    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    print(total_seconds)
    pyperclip.copy(str(total_seconds))

#def GetTime():
#    hours = raw_input("Hours: ")
#    minutes = raw_input("Minutes: ")
#    seconds = raw_input("Seconds: ")
#    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)