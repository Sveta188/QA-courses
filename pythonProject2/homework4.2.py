import sys
str = input("Enter the string which contains 8  and more symbols")
while len(str) < 8:
    str = input( "Please, enter the string, which contains 8 and more symbols")
print(str[:8])
begin_of_center = int(len(str)/2-2)
end_of_center = int(len(str)/2+2)
print(str[begin_of_center:end_of_center])
print(str[::3])
print(str[::-1])


