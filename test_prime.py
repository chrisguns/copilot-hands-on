def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

# Test cases
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(17) == True
assert is_prime(19) == True
assert is_prime(23) == True
assert is_prime(29) == True
assert is_prime(31) == True
assert is_prime(37) == True
assert is_prime(41) == True
assert is_prime(43) == True
assert is_prime(47) == True
assert is_prime(53) == True
assert is_prime(59) == True
assert is_prime(61) == True
assert is_prime(67) == True
assert is_prime(71) == True
assert is_prime(73) == True
assert is_prime(79) == True
assert is_prime(83) == True
assert is_prime(89) == True
assert is_prime(97) == True

assert is_prime(1) == False
assert is_prime(4) == False
assert is_prime(6) == False
assert is_prime(8) == False
assert is_prime(9) == False
assert is_prime(10) == False
assert is_prime(12) == False
assert is_prime(14) == False
assert is_prime(15) == False
assert is_prime(16) == False
assert is_prime(18) == False
assert is_prime(20) == False
assert is_prime(21) == False
assert is_prime(22) == False
assert is_prime(24) == False
assert is_prime(25) == False
assert is_prime(26) == False
assert is_prime(27) == False
assert is_prime(28) == False
assert is_prime(30) == False
assert is_prime(32) == False
assert is_prime(33) == False
assert is_prime(34) == False
assert is_prime(35) == False
assert is_prime(36) == False
assert is_prime(38) == False
assert is_prime(39) == False
assert is_prime(40) == False
assert is_prime(42) == False
assert is_prime(44) == False
assert is_prime(45) == False
assert is_prime(46) == False
assert is_prime(48) == False
assert is_prime(49) == False
assert is_prime(50) == False
assert is_prime(51) == False
assert is_prime(52) == False
assert is_prime(54) == False
assert is_prime(55) == False
assert is_prime(56) == False
assert is_prime(57) == False
assert is_prime(58) == False
assert is_prime(60) == False
assert is_prime(62) == False
assert is_prime(63) == False
assert is_prime(64) == False
assert is_prime(65) == False
assert is_prime(66) == False
assert is_prime(68) == False
assert is_prime(69) == False
assert is_prime(70) == False
assert is_prime(72) == False
assert is_prime(74) == False
assert is_prime(75) == False
assert is_prime(76) == False
assert is_prime(77) == False
assert is_prime(78) == False
assert is_prime(80) == False
assert is_prime(81) == False
assert is_prime(82) == False
assert is_prime(84) == False
assert is_prime(85) == False
assert is_prime(86) == False
assert is_prime(87) == False
assert is_prime(88) == False
assert is_prime(90) == False
assert is_prime(91) == False
assert is_prime(92) == False
assert is_prime(93) == False
assert is_prime(94) == False
assert is_prime(95) == False
assert is_prime(96) == False
assert is_prime(98) == False
assert is_prime(99) == False
assert is_prime(100) == False

print("All test cases passed!")