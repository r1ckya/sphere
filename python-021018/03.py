def solution1(a):
    import re
    return list(map(lambda s: int(''.join(re.findall(r'\d+', s))[::-1]), a))

def solution2(z):
    from operator import mul
    from itertools import starmap
    return list(starmap(mul, z))
    
def solution3(r):
    return list(filter(lambda x: x % 6 in (0, 2, 5), r))

def solution4(a):
    return list(filter(lambda x: x, a))

def solution5(a):
    from operator import setitem
    any(map(lambda x: setitem(x, 'square', x['width'] * x['length']), a))

def solution6(a):
    from operator import setitem
    return list(map(lambda x: setitem(x, 'square', x['width'] * x['length']) or x, a))

def solution7(a):
    from operator import setitem
    return list(map(lambda x: (lambda y: setitem(y, 'square', y['width'] * y['length']) or y)(x.copy()), a))

def solution8(a):
    from functools import reduce
    return reduce(lambda x, y: (x[0] + y['height'], x[1] + 1), a, (0, 0))

def solution9(a):
    from operator import getitem
    return list(map(lambda x: getitem(x, 'name'), filter(lambda x: x['gpa'] > 4.5, a)))

def solution10(a):
    return list(filter(lambda s: sum(map(int, s[::2])) == sum(map(int, s[1::2])), a))

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
    from copy import deepcopy

    assert solution1(['12', '25.6', '84,02', '  69-91']) == [21, 652, 2048, 1996]
    assert solution2(zip(range(2, 5), range(3, 9, 2))) == [6, 15, 28]
    assert solution3(range(20)) == [0, 2, 5, 6, 8, 11, 12, 14, 17, 18]
    assert solution4(['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')]) == [25, 'python', ('msu', '1755-01-25')]
 
    rooms = [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]

    a = deepcopy(rooms)
    assert solution5(a) is None
    assert all(x.get('square') for x in a)

    a = deepcopy(rooms)
    assert solution6(a) is not a
    assert all(x.get('square') for x in solution6(a))
    assert all(x.get('square') for x in a)

    a = deepcopy(rooms)
    assert solution7(a) is not a
    assert all(x.get('square') for x in solution7(a))
    assert not any(x.get('square') for x in a)
    
    people = [
        {'name': 'Vova', 'height': 168},
        {'name': 'Michael', 'height': 172},
        {'name': 'Diana', 'height': 175},
        {'name': 'Nastya', 'height': 164},
    ]

    assert solution8(people) == (679, 4)

    students = [
        {'name': 'Alina', 'gpa': 4.57},
        {'name': 'Sergey', 'gpa': 5.0},
        {'name': 'Nastya', 'gpa': 4.21},
        {'name': 'Valya', 'gpa': 4.72},
        {'name': 'Anton', 'gpa': 4.32},
    ]
    
    assert solution9(students) == ['Alina', 'Sergey', 'Valya']
    
    tickets = [
        '165033',
        '477329',
        '631811',
        '478117',
        '475145',
        '238018',
        '917764',
        '394286'
    ]

    assert solution10(tickets) == ['165033', '475145', '238018']
