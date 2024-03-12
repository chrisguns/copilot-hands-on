def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))


#how it works
# explain the code above line-by-line
# n > 1: check if the number is greater than 1
# all(n % i for i in range(2, int(n**0.5)+1)): check if the number is prime
# range(2, int(n**0.5)+1): generate a sequence of numbers from 2 to the square root of n
# n % i: check if n is divisible by i
# all(): return True if all elements in the iterable are true
# int(n**0.5)+1: square root of n


#how to test
#result = is_prime(17)
#print(result)  # Output: True

# create a function to do 5 unit tests of the code above
def test_is_prime():
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    print('All test cases pass')
