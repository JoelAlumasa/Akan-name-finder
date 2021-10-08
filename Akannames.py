# Ask the user for their date of birth.

year = input("what is your year of birth?  ")

month = input("what is your month of birth? ")

day = input("what is your date of birth? ")

gender = input(" What is your Gender?")

gender = gender.lower()

yearstring = str(year)
yearvalues = int(yearstring[2::])
yearcode = (yearvalues + (yearvalues // 4)) % 7

months = [1,2,3,4,5,6,7,8,9,10,11,12]
monthcode = [0,3,3,6,1,4,6,2,5,0,3,5]
chosenmonthcode = 0
centurycode = [2,0,6]
chosencenturycode = 0
isleapyear = False
leapyearcode = 0
if int(year)%4 == 0  or int(year)%400 == 0 and int(year)%100 != 0:
    isleapyear = True
for n in range(len(months)):
    if int(month) == months[n]:
        chosenmonthcode += monthcode[n]
        break
        
for n in range(len(centurycode)):
    twodigityear = yearstring[:2]
    if twodigityear == "18":
        chosencenturycode = centurycode[0]
        break
    elif twodigityear == "19":
        chosencenturycode = centurycode[1]
        break
    elif twodigityear == "20":
        chosencenturycode = centurycode[2]
        break

if isleapyear and month == "1" or month =="2":
    leapyearcode = 1
daycalculation = (yearcode + chosenmonthcode + chosencenturycode + int(day) - leapyearcode) % 7

dayofweekindex = [0,1,2,3,4,5,6]
femalenames = ["akosua", "adjoa", "abenaa", "akua", "yaa", "afia", "amma"]
malenames = ["kwasi", "kodjo", "kwabena", "kwaku", "yaw", "kofi", "kwame"]
username = ''
for num in dayofweekindex:
    if daycalculation == dayofweekindex[num]:
        if gender == "male":
            username = malenames[num]
            break
        elif gender == "female":
            username = femalenames[num]
            break
print(f"Your akan name is {username}")

