def is_prime_list(numbers):
    for num in numbers:
        for n in range(2, num):
            if num % n == 0:
                return False
    return True
