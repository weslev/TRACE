import random

# Decleration of lists
zodiac = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]
horoList = ["You will have a good week!", "You will have an ok week.", "You will be successful in your future!"]
userList = []

# Function finds the zodiac for inputted date. Checks if improper number is entered
def Selection(month, day):
    if month == 1:
        if day < 20:
            return 11
        elif day >= 20 and day <= 31:
            return  0
        else:
            return -1
    elif month == 2:
        if day <= 18:
            return 0
        elif day > 18 and day <= 28:
            return 1
        else:
            return -1
    elif month == 3:
        if day < 21:
            return 1
        elif day >= 21 and day <= 31:
            return 2
        else:
            return -1
    elif month == 4:
        if day < 20:
            return 2
        elif day > 20 and day <= 30:
            return 3
        else:
            return -1
    elif month == 5:
        if day < 21:
            return 3
        elif day >= 21 and day <= 31:
            return 4
        else:
            return -1
    elif month == 6:
        if day < 21:
            return 4
        elif day >= 21 and day <= 30:
            return 5
        else:
            return -1
    elif month == 7:
        if day < 22 and day <= 31:
            return 5
        elif day >= 22:
            return 6
        else:
            return -1
    elif month == 8:
        if day < 23:
            return 6
        elif day >= 23 and day <= 31:
            return 7
        else:
            return -1
    elif month == 9:
        if day < 23:
            return 7
        elif day >= 23 and day <= 30:
            return 8
        else:
            return -1
    elif month == 10:
        if day < 23:
            return 8
        elif day >= 23 and day <= 31:
            return 9
        else:
            return -1
    elif month == 11:
        if day < 22:
            return 9
        elif day >= 22 and day <= 30:
            return 10
        else:
            return -1
    elif month == 12 and day <= 31:
        if day < 22:
            return 10
        elif day >= 22:
            return 11
        else:
            return -1
    else:
        return -1

# Assigns random horoscope and returns the horoscope and zodiac sign in a list
def Horoscope(sign, scopes):
    choice = random.randint(0,2)
    horoscope = scopes[choice]
    userData = [sign, horoscope]
    return userData

# Runs until the user enters a valid date
while (True):
    birthMonth = int(input("Please enter your birth month: "))
    birthDay = int(input("Please enter your birth day: "))
    signNum = Selection(birthMonth, birthDay)
    sign = zodiac[signNum]
    if signNum == -1:
        print("Invalid input! Please try again.")
        continue
    else:
        break

userList = Horoscope(sign, horoList)

# Prints zodiac and horoscope
print(f"Your zodiac is: {userList[0]} \nYour horoscope is: {userList[1]}")

