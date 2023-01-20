# Twin primes are a pair of prime numbers that differ by 2. For example, 3 and 5 are twin primes,
# 5 and 7 are twin primes, and 11 and 13 are twin primes. Write a program to find all twin primes
# less than 1,000. Display the output as follows:
# (3, 5)
# (5, 7)

def is_prime(num):
    '''
        Validate if a number is prime or not
    '''
    count = 0
    if num == 1:
        return False
    for x in range(1, int(num/2 + 1)):
        if num%x == 0:
            count += 1

    return False if count >= 2 else True

def twin_prime_generator(num):
    '''
        generate twin primes till num
    '''
    twin_prime_list = []
    i = 1
    while i < num:
        if is_prime(i) and is_prime(i+2):
            twin_prime_list.append((i, i+2))
            i = i+2
        else:
            i += 1
    return twin_prime_list


def main():
    print("Twin primes less than 1000")
    twin_prime_list_gen = twin_prime_generator(1000)
    for x in twin_prime_list_gen:
        print(x)

if __name__ == "__main__":
    main()
