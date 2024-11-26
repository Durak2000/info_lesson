def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_same_digit_sum(N):
    result = []
    for i in range(N + 1):
        if all(digit_sum(i) == digit_sum(i * j) for j in range(2, 10)):
            result.append(i)
    return result

