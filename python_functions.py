def message(number):    # defining a function
    print("Enter a number: " , number)    # body of the function
message(5) 
       # calling the function

    #    2 parameters in a function
def student(firstname, lastname):  
    print("Enter your first name: ", firstname, "Enter your last name: ", lastname)
student("John", "Smith")

# positional parameter passing
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

# keyword parameter passing
def my_function(a, b, c):
    print(a, b, c)
my_function(a=1, b=2, c=3)

# mixing positional and keyword arguments
def my_function(a, b, c):
    
    print(a, "+",b,"+" ,c, "=", a+b+c)
my_function(1, 2,3)

def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James")

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)

# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
# address(s, c, p_c)

def intro(a="James Bond", b="Bond"):
     print("My name is", b + ".", a + ".")

intro()

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")

