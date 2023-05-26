import random, datetime

def getBirthdays(numDays):
    birthdays = []
    for i in range(numDays):
        startDate = datetime.date(2001,1,1)
        days = startDate + datetime.timedelta(random.randint(0,366))
        birthdays.append(days)

    return birthdays


def checkDay(days):
    count = 0
    index = 0
    for i in days:
        ind = 0
        for j in days:
            if index == ind:
                continue
            else:
                if i == j:
                    count+=1
            ind+=1
        index+=1
    return count


numDays = int(input(">How many birthdays shall I generate? "))
total = 0
for i in range(100000):
    days = getBirthdays(numDays)
    same = checkDay(days)

    if same != 0:
        total += 1

print(100*(total/100000),"%")
        
        


    
