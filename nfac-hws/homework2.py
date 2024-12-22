"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n'
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if count > 2:
            return False
    return count == 2
print(is_prime(7))

"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int:
    # write your code here
    pass

"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum
print(factorial(5))


"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    sum_vowel = 0
    for letters in range(len(s)):
        if s[letters] in ('a', 'e', 'i', 'o', 'u'):
            sum_vowel += 1
    return sum_vowel
print(count_vowels('ali'))

"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(letters: int) -> int:
    sum=0
    for digit in str(letters):
        sum=sum+int(digit)
    return sum
print(sum_of_digits(12345))


"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    b=s[::-1]
    return b
print(reverse_string("hello"))


"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    sum=0
    for i in range(n+1):
        sum=sum+(i**2)
    return sum
print(sum_of_squares(5))


"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    sequence=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        sequence.append(n)
    return sequence
print(collatz_sequence_length(6))


"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    if (year%400==0 and year%4==0):
        return True
    else:
        return False
print(is_leap_year(2000))


"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    sum=1
    for i in range(len(s)):
        if (s[i]==' '):
            sum=sum+1
    return sum
print(count_words('I love do my homeworks'))


"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    if (s==s[::-1]):
        return True
    else:
        return False
print(is_palindrome('aba'))

"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""
def sum_of_multiples(n: int, x: int, y: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            total_sum += i
    return total_sum

print(sum_of_multiples(20, 7, 11))



"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(289,578))


"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

print(lcm(6, 8))




"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""

def count_characters(s: str, c: str) -> int:
    count=0
    for i in range(len(s)):
        if(s[i]==c):
            count=count+1
    return count

print(count_characters("apple", "p"))


"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    return len(str(abs(n)))
print(digit_count(132))



"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1
print(is_power_of_two(8))



"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""
def sum_of_cubes(n: int) -> int:
    sum=0
    for i in range(n+1):
        sum=sum+(i**3)
    return sum
print(sum_of_cubes(3))


"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""

def is_perfect_square(n: int) -> bool:
    if (n**(1/2))==int(n**(1/2)):
        return True
    else:
        return False
print(is_perfect_square(16))

"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""


def is_armstrong_number(n: int) -> bool:
    a = n
    armstrong_sum = 0
    num_digits = len(str(n))
    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** num_digits
        n //= 10
    if armstrong_sum == a:
        return True
    else:
        return False
print(is_armstrong_number(153))

