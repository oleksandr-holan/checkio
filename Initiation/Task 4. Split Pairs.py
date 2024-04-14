from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    result = []
    for i in range(0, len(text), 2):
        try:
            result.append(text[i] + text[i + 1])
        except IndexError:
            result.append(text[-1] + '_')
    return result


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
