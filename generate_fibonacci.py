def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    print("Fibonacci sequence:")
    print(fib_sequence[:n])

terms = int(input("Enter the number of terms: "))
generate_fibonacci(terms)
