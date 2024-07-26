happy = "tanu kaushik"
sad = "mata"

print(happy[4])

# slicing string
substring = happy[1:4]
print(substring)

# concatenation
full_string = happy + " " + sad  
print(full_string)

# methods
# 1. replace()
print(sad.replace('a','t'))
# 2. split()
print(happy.split())
# 3. uppercase
print(happy.upper())
# 4. lowercase
print(sad.lower())
# 5. strip- Removes any leading or trailing whitespaces
print(happy.strip())

# string formatting -----f-Strings (Formatted String Literals): From Python 3.6 onwards,
#  you can use f-strings for more concise and readable string formatting.
yellow = "pot"
red = "wine"
new = "i like tea in {} and {} in glass".format(yellow,red)
print(new)