# ex.1
def add(a,b):
    return a+b
print(add(3,2))

#2
def reverse(a):
    return a[::-1]
print(reverse("12344"))

#3
def LengthOfString(a):
    total = 0
    for i in range(len(a)):
        total += 1
    return total
print(LengthOfString('rainbow'))


