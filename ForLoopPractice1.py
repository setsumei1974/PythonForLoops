'''
colors = ["red", "blue", "green"]
new_colors = []

for i in colors:
    new_colors.append(i),
    print(new_colors)

numbers_list = []

for x in range(1, 10000):
    if (x <= 1000):
        numbers_list.append(x),
        print(numbers_list),
    if (x == 1500):
        break
        print("And we are finished")

def Fizzbuzz(x):
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    if x % 3 == 0 and x % 5 == 0:
        return "Fizzbuzz"
    return x

print(Fizzbuzz(7))
'''

counter = 0

for i in range(0, 10000):
    print(i)
    counter += 1
    print(counter * 2)
    if counter == 1500:
        break

counter2 = 0

while counter2 < 1500:
    print("All is well.")
    counter2 += 5