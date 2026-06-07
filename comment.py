# print("Hello")
# This is a file in which we 
# will study about comments in python

'''Hello'''
def add(a,b):
    '''Hello'''
    print("hello")


print(add.__doc__)
def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__doc__)       # Function docstring
print(add(1, 3))         # 4
print(add(1, 3    ).__doc__) # int docstring
