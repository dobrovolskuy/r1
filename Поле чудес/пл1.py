import random

words = ["apple", "banana", "cherry", "grape", "pear"]
random_fruit = random.choice(words)
attempts = int(input("Enter the number of attempts: "))
print("You have {} attempts.".format(attempts))

guessed_letters = ["*"] * len(random_fruit)

for _ in range(attempts):
    user_guess = input("Enter a letter or a word: ")

    if len(user_guess) == 1:
        if user_guess in random_fruit:
            print("Good guess!")
            for i in range(len(random_fruit)):
                if random_fruit[i] == user_guess:
                    guessed_letters[i] = user_guess
        else:
            print("Sorry, that letter is not in the word.")
    elif user_guess == random_fruit:
        print("Congratulations! You guessed the word: {}".format(random_fruit))
        break
    else:
        print("Sorry, that's not the word.")

    word_display = "".join(guessed_letters)
    print("Current word: {}".format(word_display))

    if "*" not in guessed_letters:
        print("Congratulations! You guessed the word: {}".format(random_fruit))
        break
else:
    print("Out of attempts. The word was: {}".format(random_fruit))

