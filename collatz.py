def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage
num = int(input("Write a number"))
result = collatz_sequence(num)
print(f"Collatz sequence for {num}: {result}")