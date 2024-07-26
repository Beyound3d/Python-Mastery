def running():
    print("run")

# calling functions
running()

# with parameter
def kiss(me):
    print(f"vip lets take a sip with, {me}.")

kiss("Divya")

# return: keyword to return a value from the function.
def add(wine, divine):
    return wine + divine

darling = add("you", "me")
print(darling)

# default parameter value(= sign)

def love(years=7):
    print(f"you love me baby,for {years} times")

love()
love(1000)

# keyword argument
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Divya", message="Good morning") 


# Arbitrary Arguments:
# Use *args to pass a variable number of non-keyword arguments and **kwargs for keyword arguments.

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  # Output: Hello, Alice! Hello, Bob! Hello, Charlie!
