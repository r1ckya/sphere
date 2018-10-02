def solution1(s):
    return list(map(lambda x: x * 4, s))

def solution2(s):
    from itertools import starmap
    return list(starmap(lambda x, y: y * (x + 1), enumerate(s)))

def solution3(r):
    return [x for x in r if (bin(x).count('1') & 1) == 0]

def solution4(a):
    from functools import reduce
    return reduce(lambda x, y: x + y, a, [])

def solution5(n):
    def check(a, b):
        c = (a ** 2 + b ** 2) ** 0.5
        return c <= n and int(c) == c
    
    return [(x, y, (x ** 2 + y ** 2) ** 0.5) for x in range(1, n + 1) for y in range(x, n + 1) if check(x, y)]

def solution6(a):
    return [list(map(lambda x: x + y, a[1])) for y in a[0]]

def solution7(a):
    from operator import itemgetter
    return [list(map(itemgetter(i), a)) for i in range(len(a[0]))]

def solution8(a):
    return [list(map(int, e.split())) for e in a]

def solution9(r):
    return {chr(ord('a') + i): i ** 2 for i in r}

def solution10(a):
    return set(s.title() for s in a if len(s) > 3)

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

if __name__ == '__main__':
    assert solution1('python') == ['pppp', 'yyyy', 'tttt', 'hhhh', 'oooo', 'nnnn']
    assert solution2('python') == ['p', 'yy', 'ttt', 'hhhh', 'ooooo', 'nnnnnn']
    assert solution3(range(16)) == [0, 3, 5, 6, 9, 10, 12, 15]
    assert solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert solution5(15) == [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)]
    assert solution6(([0, 1, 2], [0, 1, 2, 3, 4])) == [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    assert solution7([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert solution8(["0", "1 2 3", "4 5 6 7", "8 9"]) == [[0], [1, 2, 3], [4, 5, 6, 7], [8, 9]]
    assert solution9(range(7)) == {'a': 0, 'b': 1, 'c': 4, 'd': 9, 'e': 16, 'f': 25, 'g': 36}
    assert solution10(['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']) == {'Alice', 'Anton', 'Kamila', 'Nastya', 'Vova'}
