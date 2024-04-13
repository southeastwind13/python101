'''
all()

The all() function returns True if all elements in the given iterable are true.
If not, it returns False.

True - If all elements in an iterable are true, or empty
False - If any element in an iterable is false
'''

a = []
b = [1, 2, 3 ,4]
c = [1, 2, 3, 4, False]
d = [1, 2, 3, 4, 0]

print(all(a))
print(all(b))
print(all(c))
print(all(d))