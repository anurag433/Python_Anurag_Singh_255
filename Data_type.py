# Data Type
var1 = 1 
var2 = True 
var3 = 10.23 
var4 = 10+3j

print(id(var1))
print(id(var2))
print(id(var3))
print(id(var4))

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#string data type

# two type of string  : single line(' ' ) and multiline (  ""   ,   '''  '''  )
#  string as array
name = "anurag"
last_name = 'singh'

print(type(name))
print(type(last_name))

# slice means access the value from given point to another point

b= "Hello"
print(b[-4:-2])

# upper case 
name = "anurag"
print(name.upper())

# lower case 
name = "ANURAG"
print(name.lower())

# remove whilespace 

a = "   hello, world   "

print(a.strip())