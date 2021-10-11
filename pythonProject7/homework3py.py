a = 12
b = 14
print(a < b and b != 16) #true
print(a < b and b < a) #false
print(a > b and a != b)# false
print(a == 12 and b == 14) #true
print(a > b or a != b) #true
print(a > b or a == b) #false
print(b > 38 or a >40) #false
print(a > 1 or  b < 18) #true
a = "abc"
b= "s"
print(a < b and a > "rtyujnjkj") #true
print(a < b and b < "x") #true
print(a < b or a > "rtyujnjkj") #true
