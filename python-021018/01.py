def A(m, n):
    A.counter += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))

def ackermann(m, n):
    A.counter = 0
    ans = A(m, n)
    ackermann.counter = A.counter
    return ans

if __name__ == '__main__':
    print(ackermann(3, 5), ackermann.counter)
    print(ackermann(3, 5), ackermann.counter)

