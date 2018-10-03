def gen(ans, n, balance):
    if n == 0:
        yield ans
        return
    if balance + 1 <= n - 1:
        ans += '('
        yield from gen(ans, n - 1, balance + 1)
        ans = ans[:-1]
    if balance > 0:
        ans += ')'
        yield from gen(ans, n - 1, balance - 1)

def brackets(n):
    yield from gen('', 2 * n, 0)

if __name__ == '__main__':
    print(*brackets(int(input())), sep='\n')