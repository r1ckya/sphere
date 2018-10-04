def binomial(n):
    cur = 1
    for k in range(n + 1):
        yield cur
        cur = (n - k) * cur // (k + 1)

if __name__ == '__main__':
    for n in map(int, input().split()):
        print(*binomial(n))
