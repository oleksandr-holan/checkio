def flat_list(array):
    result = []

    def elements(data):
        if type(data) is int:
            result.append(data)
            return 0
        return [elements(i) for i in data]
    elements(array)

    return result

# flat_list = f = lambda d: 0 * d == 0 and [d] or sum(map(f, d), [])


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
