import random
import math
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to classify numbers as prime or composite
def classify_numbers(numbers):
    primes = []
    composites = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
        elif number > 1:  # Exclude 1 as it's neither prime nor composite
            composites.append(number)
    return primes, composites

# Function to generate a list of K random numbers within limit N
def generate_random_numbers(K, N):
    return random.sample(range(1, N+1), K)

# User input for K (number of random numbers) and N (limit)
K = int(input("Enter the number of random numbers (K): "))
N = int(input("Enter the upper limit (N): "))

# Ensure K is at least 10
if K < 10:
    print("K should be at least 10. Setting K to 10.")
    K = 10

# Step 1: Generate a list of K random numbers within limit N
random_numbers = generate_random_numbers(K, N)

# Step 2: Classify the numbers into prime and composite
primes, composites = classify_numbers(random_numbers)

# Step 3: Calculate the squares of primes and square roots of composites
prime_squares = [x**2 for x in primes]
composite_square_roots = [math.sqrt(x) for x in composites]

# Step 4: Plotting the results in subplots

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Prime numbers vs their squares
axs[0].scatter(primes, prime_squares, color='blue')
axs[0].set_title('Prime Numbers vs Their Squares')
axs[0].set_xlabel('Prime Numbers')
axs[0].set_ylabel('Squares of Prime Numbers')

# Composite numbers vs their square roots
axs[1].scatter(composites, composite_square_roots, color='red')
axs[1].set_title('Composite Numbers vs Their Square Roots')
axs[1].set_xlabel('Composite Numbers')
axs[1].set_ylabel('Square Roots of Composite Numbers')

# Show the plot
plt.tight_layout()
plt.show()
