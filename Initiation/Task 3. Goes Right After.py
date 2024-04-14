# def goes_after(word: str, first: str, second: str) -> bool:
#     if first == second:
#         return False
#     for i in range(len(word) - 1):
#         if word[i] == second:
#             return False
#         if word[i] == first:
#             if word[i + 1] == second:
#                 return True
#             return False
#     return False

# def goes_after(word: str, first: str, second: str) -> bool:
#     try:
#         return word.index(second) - word.index(first) == 1
#     except ValueError:
#         return False

goes_after = lambda word, first, second: word.index(second) - word.index(first) == 1 \
                                        if first in word and second in word else False

print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after('almaz', 'm', 'a') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
