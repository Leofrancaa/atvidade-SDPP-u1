import time
import concurrent.futures
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def read_input(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    return numbers

def write_output(filename, primes):
    with open(filename, 'w') as f:
        for p in primes:
            f.write(f"{p}\n")

def process_sequential(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes

def process_parallel(numbers, num_threads):
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(is_prime, n): i for i, n in enumerate(numbers)}
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            results[index] = future.result()
    sorted_results = [results[i] for i in range(len(numbers))]
    primes = [numbers[i] for i, is_p in enumerate(sorted_results) if is_p]
    return primes

