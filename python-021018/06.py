def binominal(n):
    cur = 1
    for k in range(n + 1):
        yield cur
        cur = (n - k) * cur // (k + 1)

if __name__ == '__main__':
    from sys import stdin
    for line in stdin.readlines():
        for n in map(int, line.split()):
            for x in binominal(n):
                print(x, end=' ')
            print()

