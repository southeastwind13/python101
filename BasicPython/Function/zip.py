'''
zip 

- Takes iterables, aggregate them in a tuple, and return it.
- We can zip more than 2 iterables in the same time.
- The size of item in output tuple will be the size of the smallest iterables
'''

a = ("John", "Charles", "Mike",)
b = ("Jenny", "Christy", "Monica", "vicky")
c = ("a", "b")

x = zip(a, b, c)
print(list(x))