a = [1, 2, 3]
a = (1, 2, 3)

print(bool(a.__hash__))
print(list.__hash__)

# if hash(a):
#     print(hash(a))
# else:
#     print(a)