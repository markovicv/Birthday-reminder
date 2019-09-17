import os,time,subprocess

def isBirthdayToday(path):
     
    filename = open(path,'r')
    today = time.strftime('%d/%m')
    isBt = False
    for dateLine in filename:
        if today in dateLine:
            isBt = True
            dateLine = dateLine.split(' ')
            birthdayPerson = dateLine[1]+" "+dateLine[2]
            os.system('notify-send "BIRTHDAY!!!" "'+birthdayPerson+'"')
    if not isBt:
        os.system('notify-send "NO BIRTHDAYS TODAY"')




path = '/home/vukasin/python/birthdayCheck/birthdays.txt'
isBirthdayToday(path)






