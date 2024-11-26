def to_binary(n):
    if n > 1:
        to_binary(n // 2)
    print(n % 2, end='')

to_binary(10) 
   