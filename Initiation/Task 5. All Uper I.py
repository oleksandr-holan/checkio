from string import ascii_letters


def is_all_upper(text: str) -> bool:
    return text.isupper() or not any([c in ascii_letters for c in text])
    # return text.upper() == text


print("Example:")
print(is_all_upper("ALL UPPER"))

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
