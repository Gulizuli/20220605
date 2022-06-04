def count_bits(n):
    count = 0
    while n != 0:
        if (n%2):
            count += 1
        n = int(n/2)
    return count

print(count_bits(5555))
