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

#4
def SumOfStrings(a,b):
    return a+b
print(SumOfStrings('Hello','Ali'))

#5
def CheckOfVowel(a):
    return a.lower() in 'aeuyio'
print(CheckOfVowel('A'))

#6
def SwapCharacters(a):
    new_str=a[-1]+a[1:-1]+a[0]
    return new_str
print(SwapCharacters('Wood'))
#7
def Surface(a,b):
    surface=a*b
    return surface
print(Surface(3,4))

#8
def Upper(a):
    return a.upper()
print(Upper('was'))