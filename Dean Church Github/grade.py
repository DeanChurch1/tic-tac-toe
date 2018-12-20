##gradelist = []
##
##
##
##
##
##def getGrade(gradelist):
##    maxGrade = 100
##    while True:
##        grade = input("enter in a grade (to exit press space bar)")
##        if grade == " ":
##            break
##        else:
##            x = int(grade)
##            if grade.isdigit() and x <= maxGrade:
##                grade = float(grade)
##                gradelist.append(grade)
##            elif x>= maxGrade:
##                q = input("are you sure this "+grade+" is a good grade y or n")
##                if q == 'y':
##                    grade = float(grade)
##                    gradelist.append(grade)    
##            else:
##                print("thats not a good grade")
##
##
##def avgfunction(gradelist):
##    sumgrade = 0
##    for grade in gradelist:
##        sumgrade += grade
##    avg = sumgrade / len(gradelist)
##    return avg
##
##def main(gradelist):
##    getGrade(gradelist)
##    avg = avgfunction(gradelist)
##    print("your grade is",avg)
##
##
##main(gradelist)
start = 5
stop = 1000
stepvalue = 5
for i in range(stop,start,-5):
    print(i)


