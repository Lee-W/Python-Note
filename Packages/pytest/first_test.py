def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_func_right():
    assert func(3) == 4


def test_func_with_loop():
    for i in range(99999):
        pass
    assert func(3) == 4
