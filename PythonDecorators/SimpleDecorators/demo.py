def funcName(func):
    def wrapper():
        print('the given function is going to run')
        func()
    return wrapper

def greet():
    print("hello")

def add(a,b):
    print(a+b)

# g = funcName(greet)
# g()

s = funcName(add(2,15))
s
