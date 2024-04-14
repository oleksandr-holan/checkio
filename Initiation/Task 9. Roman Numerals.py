def checkio(data):
    arr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    string = ''
    for i, c in enumerate(str(data)[::-1]):
        n = int(c)
        r = ''
        if n == 9:
            r += arr[i * 2] + arr[i * 2 + 2]
            n -= 5
        elif n == 4:
            r += arr[i * 2] + arr[i * 2 + 1]
            n -= 5
        else:
            if 4 < n < 9:
                r += arr[i * 2 + 1]
                n -= 5
            if 0 < n < 4:
                for _ in range(n):
                    r += arr[i * 2]
        string = r + string
    return string


# def checkio(x):
#     a, r = "", {}
#     for i in range(3):
#         p, (j, c, d) = 10 ** i, "IVXLCDM"[2 * i:][:3]
#         r.update({p: j, 4 * p: j + c, 5 * p: c,  9 * p: j + d, 10 * p: d})
#     for k in reversed(sorted(r)):
#         a += x // k * r[k]
#         x %= k
#     return a


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(6))
    assert checkio(6) == 'VI', '6'
    print(checkio(76))
    assert checkio(76) == 'LXXVI', '76'
    print(checkio(499))
    assert checkio(499) == 'CDXCIX', '499'
    print(checkio(3888))
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print(checkio(50))
    print('Done! Go Check!')
