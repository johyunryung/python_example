def reverse_num(n):
    n1 = str(n)
    n1 = ''.join(reversed(n1))
    a = int(n)
    return n+a , n-a, n*a, a/n

print(reverse_num(22))
