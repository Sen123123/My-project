Alp = input("Write a sentence:")
count = 0

for char in Alp:
    if char.isalpha():
        count += 1

print("Number of characters/ alphabets you have typed:",count)