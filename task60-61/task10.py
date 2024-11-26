def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
    def amicable_numbers(limit):
    pairs = []
    for i in range(1, limit):
        j = sum_of_divisors(i)
        if j < limit and i != j and sum_of_divisors(j) == i:
            pairs.append((i, j))
    return pairs

