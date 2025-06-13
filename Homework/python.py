Alp = input("Write a sentence:")
count = 0

vowels = "aeiouAEIOU"

for char in Alp:
    if char in vowels:
        count += 1

print("Number of characters/ alphabets you have typed:",count)