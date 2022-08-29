import pytest

@pytest.mark.parametrize('strA, strB, exp', [
    (['apple', 'orange', 'grape'], ["banana", "kivi"], ['apple', 'orange', 'grape', 'banana', 'kivi'])
])

def test_appendNone(strA, strB, exp):
    assert strA.append(strB) == None



@pytest.mark.parametrize("str_a, str_b, expected", [
    (["apple", "orange", "grape"], "banana", ["apple", "orange", "grape", "banana"]),
    (["apple", 'cherry', "orange", "grape"], "banana", ["apple", 'cherry', "orange", "grape", "banana"]),
    (["apple", 1, "orange", "grape"], "banana", ["apple", 1, "orange", "grape", "banana"])
])
def test_append(str_a, str_b, expected):
    str_a.append(str_b)
    assert str_a == expected


@pytest.mark.parametrize("str_a, expected", [
    (["apple", "orange", "grape"], [])
])
def test_clear(str_a, expected):
    str_a.clear()
    assert str_a == expected

@pytest.mark.parametrize("str_a, expected", [
    (["apple", "orange", "grape"], ["apple", "orange", "grape"])
])
def test_copy(str_a, expected):
    x = str_a.copy()
    print(x)
    assert x == expected


@pytest.mark.parametrize("str_a, str_b, expected", [
    (["apple", "orange", "grape", 'apple'], 'apple', 2),
    (["apple", "orange", "grape", 1, 2, 3, 4, 5, 5, 5, 'apple'], 5, 3),
    (["apple", "orange", "grape", 'apple', 1, 1, 1, 1], 1, 4)
])
def test_count(str_a, str_b, expected):
     assert str_a.count(str_b) == expected


@pytest.mark.parametrize("str_a, str_b, expected", [
    (["apple", "orange", "grape", 'apple'], ['apple'], ["apple", "orange", "grape", 'apple', 'apple']),
    (["apple", "orange", "grape"], [1], ["apple", "orange", "grape", 1]),
    (["apple", "orange", "grape", 'apple'], [1, 1, 1, 1], ["apple", "orange", "grape", 'apple', 1, 1, 1, 1])
])
def test_extend(str_a, str_b, expected):
    str_a.extend(str_b)
    assert str_a == expected


@pytest.mark.parametrize("str_a, str_b, expected", [
    (["apple", "orange", "grape", 'apple'], 'apple', 0),
    (["apple", "orange", "grape", 'apple', 1], 1, 4),
    (["apple", "orange", "grape", 'apple', 1, 1, 1, 1], 1, 4),
    (["apple", "orange", "grape", 'apple', 1, 1, 1, 1], 'apple', 0)
])
def test_index(str_a, str_b, expected):
    x = str_a.index(str_b)
    assert x == expected


@pytest.mark.parametrize("str_a, str_b, pos, expected", [
    (["apple", "orange", "grape", 'apple'], 'garlick', 1, ["apple", 'garlick', "orange", "grape", 'apple']),
    (["apple", "orange", "grape", 'apple'], ('garlick', 'onion'), 1, ["apple", ('garlick', 'onion'), "orange", "grape", 'apple']),
    (["apple", "orange", "grape", 'apple'], ('garlick', 'onion'), 3, ["apple", "orange", "grape", ('garlick', 'onion'), 'apple'])
])
def test_insert(str_a, str_b, pos, expected):
    x = str_a.insert(pos, str_b)
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize("str_a, args, expected", [
    (["apple", "orange", "grape", 'vine'], (1, ), ["apple", "grape", 'vine']),
    (["apple", "orange", "grape", 'vine'], (), ["apple", "orange", "grape"]),
    (["apple", "orange", "grape", ('garlick', 'onion')], (3, ), ["apple", "orange", "grape" ]),
])
def test_pop(str_a, args, expected):
    str_a.pop(*args)
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize("str_a, pos, expected", [
    (["apple", "orange", "grape", 'vine'], 1, 'orange'),
    ])
def test_pop1(str_a, pos, expected):
    x = str_a.pop(pos)
    print(x)
    assert x == expected


@pytest.mark.parametrize("str_a, expected", [
    (["apple", "orange", "grape", 'vine', 'blueberry'],  ["apple", "orange", "grape", 'vine']),
])
def test_pop2(str_a, expected):
    str_a.pop()
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize('str_a, arg, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], 'apple', ["orange", "grape", 'vine', 'blueberry']),
    (["apple", "orange", "grape", 'vine', 'blueberry'], 'grape', ['apple', "orange", 'vine', 'blueberry']),
    (["apple", "orange", "grape", 'vine', 'blueberry'], 'blueberry', ["apple", "orange", "grape", 'vine',])
])
def test_remove(str_a, arg, expected):
    str_a.remove(arg)
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], ['blueberry', 'vine', "grape", "orange", 'apple']),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
])
def test_reverse(str_a, expected):
    str_a.reverse()
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], ['apple', 'blueberry', "grape", "orange", 'vine']),
    ([5, 4, 3, 10, 2, 1], [1, 2, 3, 4, 5, 10]),
])
def test_sort(str_a, expected):
    str_a.sort()
    print(str_a)
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], ['vine', "orange", "grape", 'blueberry', 'apple']),
    ([5, 4, 3, 10, 2, 1], [10, 5, 4, 3, 2, 1]),
])
def test_sortDesc(str_a, expected):
    str_a.sort(reverse=True)
    print(str_a)
    assert str_a == expected





@pytest.mark.parametrize('str_a, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], ['vine','apple', "grape", "orange", 'blueberry', ]),
])
def test_sortLen(str_a, expected):
    def get_len(item):
        return len(item)
    str_a.sort(key=get_len)
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    (["apple", "orange", "grape", 'vine', 'blueberry'], ['vine', 'apple', "grape", "orange", 'blueberry']),
])
def test_sortLenLamda(str_a, expected):
    str_a.sort(key=lambda x: len(x))
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    ([
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
], [
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'Ford', 'year': 2005},
    {'car': 'VW', 'year': 2011},
    {'car': 'BMW', 'year': 2019}
]),
])
def test_sortYear(str_a, expected):
    def get_year(item):
        return item['year']
    str_a.sort(key=get_year)
    assert str_a == expected



@pytest.mark.parametrize('str_a, expected', [
    ([
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
], [
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'Ford', 'year': 2005},
    {'car': 'VW', 'year': 2011},
    {'car': 'BMW', 'year': 2019}
]),
])
def test_sortYearLambda(str_a, expected):
    str_a.sort(key=lambda x: x['year'])
    assert str_a == expected


@pytest.mark.parametrize('str_a, expected', [
    ([
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
], [
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011},
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000}
]),
])
def test_sortYearLambdaReverso(str_a, expected):
    str_a.sort(reverse=True,key=lambda x: x['year'])
    assert str_a == expected



