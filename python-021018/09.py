from copy import deepcopy

class FragileDict:
    def __init__(self, data=None):
        self._lock = False
        self._data = deepcopy(data) or dict()

    def __getitem__(self, key):
        if self._lock:
            return self._data[key]
        else:
            return deepcopy(self._data[key])

    def __setitem__(self, key, value):
        if self._lock:
            self._data[key] = value
        else:
            raise RuntimeError('Protected state')

    def __contains__(self, key):
        return key in self._data

    def __enter__(self):
        self._lock = True
        self._tmp = deepcopy(self._data)

    def __exit__(self, exc_type, exc_value, tb):
        self._lock = False
        if exc_type is not None:
            self._data, self._tmp = self._tmp, self._data
            print('Exception has been suppressed.')
        else:
            self._data = deepcopy(self._data)
        del self._tmp
        return True

if __name__ == '__main__':
    d = FragileDict({'key': []})

    with d:
        a = d['key']
        d['key'].append(10)
        a.append(10)

    a.append(10)

    print(a == [10, 10, 10] and d['key'] == [10, 10])
