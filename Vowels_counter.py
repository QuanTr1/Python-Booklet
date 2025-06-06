sentence = input("Give me a sentence: ")

numberE = 0
vowel = "aeiou"

for letter in sentence:
    if letter in vowel:
        numberE += 1
        
print ("The number of vowel letters in the sentence is: " ,numberE)