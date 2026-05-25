# Functions with input

def greet_with_name(name, age, skin_color):
    print(f"Hello {name}")
    print(f"I heard you said I'm {skin_color}")
    print(f"How do you do know I am {age} years old?")


greet_with_name(name = "ola", age =22, skin_color = "black")

s1 = ['t', 'r', 'u', 'e']
s2 = ['l', 'o', 'v', 'e']


def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()

    true_score = 0
    for letter in s1:
        true_score += combined_name.count(letter)

    love_score = 0
    for letter in s2:
        love_score += combined_name.count(letter)

    score = int(str(true_score) + str(love_score))
    print(score)

calculate_love_score(name1="Angela Yu", name2 = "Jack Bauer")