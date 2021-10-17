names = list(map(str, input("Enter the name through space").split()))
print(names)
if len(names) == 0:
    print("likes() -> \"no one likes this\"")
elif len(names) == 1:
    string = "likes(\"{name}\") -> \"{name} likes this\""
    print(string.format(name=names[0]))
elif len(names) == 2:
    print("likes(\"{0}\", \"{1}\") -> \"{0} and {1} like this\"".format(names[0], names[1]))
elif len(names) == 3:
    print("likes(\"{0}\", \"{1}\", \"{2}\") -> \"{0}, {1} and {2} like this\"".format(names[0], names[1], names[2]))
else:
    counts = len(names) - 2
    part = "likes(\"{0}\", \"{1}\", \'....\') -> \"{0}, {1} \"".format(names[0], names[1])
    part1 = "and {count} others like this"
    part1 = part1.format(count=counts)
    print(part + part1)





