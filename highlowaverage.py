#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

numInput = open("numbers.txt")

sum = 0
count = 0
numList = []

for curLine in numInput:
    tempInt = int(curLine)
    count += 1
    sum += tempInt
    numList.append(tempInt)

numInput.close()

max = max(numList)
min = min(numList)
average = sum / count

print(f"Total amount of numbers: {count}")
print(f"Sum of all numbers: {sum}")
print(f"Average: {average}")
print(f"Highest number: {max}")
print(f"Lowest number: {min}")
