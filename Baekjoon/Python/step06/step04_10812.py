N, M = map(int, input().split())

# Initialize the basket list with numbers from 1 to N
baskets = list(range(1, N + 1))

# Iterate through the M rotation operations
for _ in range(M):
    # Read the values of i, j, and k for each operation
    i, j, k = map(int, input().split())

    # Adjust the indices to be zero-based
    i -= 1
    k -= 1

    # Rotate the baskets
    baskets = baskets[:i] + baskets[k:j] + baskets[i:k] + baskets[j:]

# Print the final order of the baskets separated by spaces
print(' '.join(map(str, baskets)))
