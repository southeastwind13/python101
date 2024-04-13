'''
Decorator

Function in Python is a object then function can receive another function as 
an input and return another function as an output.

Python has a customize function

It is a function the input another function and wrap it with some logic before
return the function with wrapper to outside so you can modify the logic of the
input function.
'''

from time import sleep


def make_star(func):

    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper

def make_percentage(func):

    def wrapper(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return wrapper

'''
Decorator will apply from button to top
'''
@make_percentage
@make_star
def print_test(b:str):
    print("test" + b)

# make_percentage(make_star(print_test("data")))


def decorator(retries: int = 3, delay: float = 1):

    if retries < 1 or delay <= 0:
        raise ValueError('Retry should grater than one!')
    
    if delay <= 0:
        raise ValueError('Delay should grater than zero!')

    def inner(func):

        def wrapper():
            print("inside wrapper")
            print("*" * 10)
            func()
            print("*" * 10)

        return wrapper
    return inner

@decorator(retries=3, delay=1)
def test_greeting():
    print("hello")


test_greeting()


# def decorator(*args, **kwargs):
#     print("Inside decorator")
     
#     def inner(func):
         
#         # code functionality here
#         print("Inside inner function")
#         print("I like", kwargs['like']) 
         
#         func()
         
#     # returning inner function    
#     return inner
 
# @decorator(like = "geeksforgeeks")
# def my_func():
#     print("Inside actual function")



'''
def retry(number_retries=3, number_delay=1):
    def inner(func:callable):
        def wrapper(*args, **kwargs):
            print("start wrapper")
            func(*args, **kwargs)
            print("end wrapper")
        return wrapper
    return inner
    

@retry()
def greeting(name:str, lastname:str):
    print(name + " " + " Lastname: " + lastname + " " + "hello")

greeting("Pong", "wong")
'''