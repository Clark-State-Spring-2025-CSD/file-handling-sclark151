#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

wordInput = open("words.txt")

palindrome = 0
wordList = []

for curLine in wordInput:
    tempStr = str(curLine.strip())
    wordList.append(tempStr)
    if tempStr == tempStr[::-1]:
        palindrome += 1

wordInput.close()

print(f"There are {palindrome} palindromes in the file.")
