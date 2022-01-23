def first():
    for i in [1, 2, 3, 4, 5]:
        print(i)

def second():
    for letter in "mango":
        print(letter)

def third():
    for x in range(1, 11, 2):
        print(x)

def fourth():
    counter = 0
    while(counter <=100):
        print(counter)
        counter = counter + 1

# Usage in List Comprehensions
A = [i for i in range(1, 30) if not i%5]
B = list(range(5, 31, 5))