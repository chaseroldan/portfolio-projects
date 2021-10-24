print("Welcome to the Python Quiz!")

playing = input("Do you want to play? (yes or no )")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What bundles data and functionality together by creating a new type of object and allowing new instances of that type to be made? A- Variable B- Method C- Function D- Class ")
if answer.lower() == "d":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is a block of code which only runs when it is called and can have data, known as parameters, passed to it? A- Variable B- Method C- Function D- Class ")
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("is a function that is available for a given object because of the object's type? A- Variable B- Method C- Function D- Class ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is a reserved memory location to store values? A- Variable B- Method C- Function D- Class ")
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")