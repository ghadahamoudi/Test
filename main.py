#Variable
from socketserver import ThreadingUDPServer

first_name = "Bro"
food ="Pizza"
email = "contact.ghadahamoudi@gmail.com"
print(first_name)
print(food)
print(first_name)
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"your email {email}")

age = 25
quantity = 3
num_of_students = 30
print(age)

print(f"your age {age}")
print(f"your quantity {quantity}")
print(f"your number of students {num_of_students}")

price = 10.99
gpa = 3.2
distance = 5.5

print(f"price {price}")
print(f"gpa {gpa}")
print(f"distance {distance} KM")

is_student = True
if is_student:
    print("Hello student")
else:
    print("Hello you qre not student")


for_sale = True
if for_sale:
    print("hello for sale")
else :
    print("Not for Sale")

is_online = True
if is_online:
    print("Hello online")
else:
    print("Not for online")



#Type Casting

name = "Ghada"
age = 26
gpa = 3.2
is_student = True

print(int(gpa))
print(type(age))
print(type(gpa))
print(type(is_student))
print("Hello there i'm Ghada Hamoudi")



# input() input function
fname = input("What is your name?")
print(f"Hello {fname}")

age = input("What is your age?")
age = int(age)
age = age + 1
print(f"your age {age}")
