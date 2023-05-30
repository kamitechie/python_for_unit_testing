import math

# Python exercises

def exercise_reverse_name():
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    full_name = name + " " + last_name
    reverse_name = full_name[::-1]
    print(reverse_name)


def exercise_num_to_tuple():
    numbers = input("Enter numbers: ")
    numbers_list = numbers.split(",")
    numbers_tuple = tuple(numbers_list)
    print(f"List: {numbers_list}\nTuple: {numbers_tuple}")


def exercise_sphere_volume():
    r = 6
    volume = (4/3)*math.pi*r**3
    return print(f"Sphere volume: {volume}")


