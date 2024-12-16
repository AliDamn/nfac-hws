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
#9
def Even(a):
    if a%2==0:
        return 'yes'
    else:
        return 'no'
print(Even(4))

#10
def TheFirstThree(a):
    return a[0:3]
print(TheFirstThree('homework'))

#11
def Inter(a,b):
    return f"Hello {a},my age is {b}"
print(Inter('Ali',8))

#12
def stringSlicing(s):
    return s[2:6]
print(stringSlicing("HelloWorld"))
#13
def TypeConversion(num_str):
    return int(num_str)
print(TypeConversion("42"))
#14
def repetition(word):
    return word*3
print(repetition("Hi"))
#15
def calculate_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder
print(calculate_remainder(17, 4))
#16
def floatDivision(x, y):
    return x / y
print(floatDivision(22, 7))
#17
def count(sentence, char):
    return sentence.count(char)
print(count("banana", "a"))
#18
def sequences():
    return "She said, \"Hello, world!\""
print(sequences())
#19
def MultiLineString():
    return """This is the first line.
This is the second line.
This is the third line."""
print(MultiLineString())
#20
def exponentiation(base, exponent):
    return base ** exponent
print(exponentiation(3, 4))
#.






