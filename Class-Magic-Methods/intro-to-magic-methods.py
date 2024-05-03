# A hook is a procedure that intercepts a process at some point in its execution

print(3.3 + 1.1)
print(3.3.__add__(1.1))

print(len([1, 2, 3]))
print([1, 2, 3].__len__())


print( "h" in "hello")
print("hello".__contains__("h"))


print(["a", "b", "c"][2]) 
print(["a", "b", "c"].__getitem__(2))